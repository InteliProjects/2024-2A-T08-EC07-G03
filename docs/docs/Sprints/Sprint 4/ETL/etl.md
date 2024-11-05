---
title: ETL
sidebar_position: 2
description : Construção do ETL na sprint 4
---

# Introdução

O processo de ETL (Extract, Transform, Load) é uma etapa essencial em qualquer projeto que envolva a manipulação de grandes volumes de dados, especialmente em machine learning. A sigla ETL se refere à extração (Extract) dos dados de diversas fontes, à transformação (Transform) desses dados para garantir sua adequação e à carga (Load) dos dados processados em um ambiente onde possam ser utilizados para análises ou modelos preditivos. Esse fluxo garante que os dados brutos possam ser convertidos em um formato útil e otimizado para as necessidades específicas do projeto.

Na primeira fase, a **extração**, os dados são recuperados de diferentes fontes, como bancos de dados, APIs ou arquivos fornecidos por parceiros. É crucial que esse processo de extração esteja de acordo com o que foi previamente definido no fluxo do modelo, ou seja, de que maneira os dados serão recebidos e com que frequência. Para garantir que o modelo esteja sempre atualizado, o processo de extração deve ser bem planejado e automatizado, permitindo a recuperação eficiente de novos dados para treinamento ou retreinamento do modelo preditivo.

A segunda fase é a **transformação**, onde os dados extraídos passam por uma série de operações para garantir que estejam no formato correto para serem utilizados no modelo. Isso inclui limpeza, formatação, agregação e outras formas de processamento para garantir a integridade dos dados e eliminar inconsistências. Alinhar esse processamento ao fluxo do modelo é fundamental, pois os dados precisam ser preparados de forma que o modelo possa ser treinado com as informações mais relevantes e úteis, maximizando sua eficácia.

Por fim, na etapa de **carga**, os dados transformados são armazenados em um local adequado, como um data warehouse ou banco de dados específico, onde ficarão disponíveis para serem usados no treinamento ou retreinamento do modelo. Esse ambiente de armazenamento precisa ser acessível e otimizado para que o modelo possa consumir os dados de maneira eficiente, permitindo um ciclo contínuo de treinamento e retreinamento, conforme novos dados são extraídos e processados. [1]

O processo de ETL, portanto, é o backbone da preparação de dados, permitindo que informações brutas se tornem a base para decisões inteligentes no modelo preditivo. A partir desses conceitos sobre ETL, todo o banco de dados do projeto foi estruturado e construído. Para ter uma visão da movimentação dos dados como um todo, um diagrama ETL foi desenvolvido:

<p align="center"><b> Figura 1 - Diagrama ETL</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/ETL.jpg').default} alt="Diagrama ETL"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>

Agora vamos detalhar cada uma das etapas do processo de ETL.

## Carregamento dos arquivos XLSX

A primeira etapa do processo de ETL é a extração dos dados brutos, que estão armazenados em arquivos XLSX. Estamos considerando arquivos XLSX, porque é o formato padrão dos relatórios fornecidos pela empresa parceira. Aqui recebemos 3 tipos tipos de arquivos: o de falhas, status e resultados.

Esse carregamento, é feito atráves da rota `/retrain` que é todo o começo do processo de re-treinamento do modelo e ETL.

## Formatar nomes dos arquivos e sobre no datalake

Após o carregamento dos arquivos, nos pegamos os arquivos, mudamos o nome deles para o padrão `name_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_{tipo de arquivo}_{{tipo de arquivo}.filename}'` e salvamos no datalake.

Segue um exemplo de como é feito a formatação do nome do arquivo:

```python

        # Listas para guardar os nomes dos arquivos de cada tipo
        resultado_names = []
        falhas_names = []
        status_names = []

        # Renomear e processar os arquivos de resultado
        for resultado in resultados:
            name_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_resultado_{resultado.filename}'
            await upload_file(resultado, name_file)  # Subir arquivo no Data Lake (simulação)
            resultado_names.append(name_file)

        # Renomear e processar os arquivos de falhas
        for falha in falhas:
            name_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_falhas_{falha.filename}'
            await upload_file(falha, name_file)  # Subir arquivo no Data Lake (simulação)
            falhas_names.append(name_file)

        # Renomear e processar os arquivos de status
        for stat in status:
            name_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_status_{stat.filename}'
            await upload_file(stat, name_file)  # Subir arquivo no Data Lake (simulação)
            status_names.append(name_file)
            
        # Excluir arquivos originais
        for file in resultado_names + falhas_names + status_names:
            if os.path.exists(file):
                os.remove(file)
                
        print(f"Arquivos processados: {resultado_names}, {falhas_names}, {status_names}")

```

## Processamento de cada tipo de arquivo e pegamos os dados necessários de cada um

Tendo todos os arquivos no datalake, passamos os nomes deles para essa função `process_data_datawarehouse` que é responsável por pegar os dados necessários de cada arquivo e salvar no datalake. Para fazer isso, passamos por cada arquivo e fazemos o tratamento necessário para pegar os dados necessários. Segue o código:

```python

            for file in resultado_names:
        try:
            file_content = await download_file(file)
            
            file_content = file_content['content']
            
            print(f'{file_content}')

            if file.endswith('.xlsx'):
                df = pd.read_excel(file_content)
            elif file.endswith('.csv'):
                df = pd.read_csv(file_content.decode('utf-8'))
            else:
                raise ValueError(f"Formato de arquivo não suportado: {file}")
            
            # Processamento do DataFrame
            df = await resultado_processing(df)
            df_resultados.append(df)


        except Exception as e:
            print(f"Erro ao processar o arquivo {file}: {str(e)}")
            continue

        
    print(f'Processed {len(df_resultados)} files')
        
    # Merge dos dataframes de resultados
    
    df_resultado = pd.concat(df_resultados, ignore_index=True)
        
    df_status_list = []
    
    
    for file in status_names:
        try:
            file_content = await download_file(file)
            
            file_content = file_content['content']
            
            print(f'{file_content}')

            if file.endswith('.xlsx'):
                df = pd.read_excel(file_content)
            elif file.endswith('.csv'):
                df = pd.read_csv(file_content.decode('utf-8'))
            else:
                raise ValueError(f"Formato de arquivo não suportado: {file}")
            
            # Processamento do DataFrame
            df = await status_processing(df)
            df_status_list.append(df)


        except Exception as e:
            print(f"Erro ao processar o arquivo {file}: {str(e)}")
            continue
    
        
    # Merge dos dataframes de status
    
    df_status = pd.concat(df_status_list, ignore_index=True)
        
    df_falhas = []
    
    for file in falhas_names:
        try:
            file_content = await download_file(file)
            
            file_content = file_content['content']
            
            print(f'{file_content}')

            if file.endswith('.xlsx'):
                df = pd.read_excel(file_content)
            elif file.endswith('.csv'):
                df = pd.read_csv(file_content.decode('utf-8'))
            else:
                raise ValueError(f"Formato de arquivo não suportado: {file}")
            
            # Processamento do DataFrame
            df = await falhas_processing(df)
            df_falhas.append(df)


        except Exception as e:
            print(f"Erro ao processar o arquivo {file}: {str(e)}")
            continue

```

### Processamento dos dados de resultados


```python

async def resultado_processing(df):
    print(df.columns)

    df.columns = df.iloc[0]

    df = df.drop([0]).reset_index(drop=True)

    print(df.columns)
    
    # df = df.drop(columns=[np.nan])

    df.drop(['ID', 'STATUS', 'UNIT', 'VALUE_ID', 'VALUE'], axis=1, inplace=True)
    
    df = df[df['NAME'] != 'SECTION_ZP8_00000001']
    
    # Criar uma tabela pivô onde cada NAME se torna uma coluna
    df = df.pivot_table(index='KNR', columns='NAME', aggfunc='size', fill_value=0)

    # Alterar os valores diferentes de zero para 1 (para indicar que aquele KNR tem dados para aquele NAME)
    df = (df > 0).astype(int)

    # Resetar o índice para trazer KNR de volta como coluna
    df_processed = df.reset_index()
    
    return df_processed

```

Detalhando um pouco mais, nos pegamos os dados de resultados, dropamos as colunas necessarias, filtramos apenas os dados com o NAME 'SECTION_ZP8_00000001' e fazemos um pivot table para que cada NAME se torne uma coluna. Depois disso, alteramos os valores diferentes de zero para 1 e resetamos o índice para trazer KNR de volta como coluna.

### Processamento dos dados de falhas

```python

async def falhas_processing(df):
    
    # Definir a linha correta como cabeçalho
    df_falhas = df.copy()
    df_falhas.columns = df_falhas.iloc[1]
    df_falhas = df_falhas[2:]

    # Resetar o índice do DataFrame
    df_falhas.reset_index(drop=True, inplace=True)
    
    df_falhas.dropna(axis=1, how='all', inplace=True)
    
    # Pegar a terceira linha como cabeçalho
    
    # df_falhas.columns = df_falhas.iloc[3]
    
    print(df_falhas.head())
    print(df_falhas.columns)
    
    df_falhas.drop(['MODELO',     'COR',   'MOTOR', 'ESTACAO', 'USUARIO',   'HALLE',   'FALHA',    'DATA'], axis=1, inplace=True)
    
    df_falhas = df_falhas.drop_duplicates()       
    
    return df_falhas

```

Detalhando um pouco mais, nos pegamos os dados de falhas, dropamos as colunas necessarias, resetamos o índice do DataFrame, dropamos as colunas que não são necessárias e dropamos as linhas duplicadas. Nessa precisamos apenas dos KNRs que tiveram falhas.

### Processamento dos dados de status

```python
async def status_processing(df):
    
    # Processamento dos dados de status
    
    # Exibir as colunas originais
    print(df.columns)

    # Dropar as colunas que não são necessárias
    df = df.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'])

    # Exibir as colunas depois da alteração
    print(df.columns)

    # Filtrar as linhas onde a coluna STATUS não é nula
    df_tst = df[df["STATUS"].notnull()]
    
    df_tst['DATA'] = pd.to_datetime(df_tst['DATA'], errors='coerce')

    # df_tst = df_tst.drop(columns=["Unnamed: 0", "Unnamed: 1", "Unnamed: 2", "Unnamed: 3"])
        
    ZP7 = ['M695', 'M698', 'M701', 'M702', 'M704', 'M711', 'M712', 'M721', 'M722']
    ZP5 = ['R640', 'R650', 'R700', 'R754']
    ZP5A = ['L534', 'L535', 'L536', 'L537', 'L538', 'L539', 'L541', 'L542', 'L543', 'L544', 'L545', 'L546', 'L547', 'L548']
    ZP6 = ['M599', 'M591', 'M592', 'M593', 'M594', 'M595', 'M596', 'M643', 'M644', 'M647', 'M648', 'M651', 'M652', 'M655', 'M656', 'M673', 'M674', 'M677', 'M678', 'M681', 'M682']
    CAB = ['M619', 'M643', 'M644', 'M655', 'M656', 'M673', 'M674']
    
        # Combine todas as listas em uma única lista
    all_stations = ZP7 + ZP5 + ZP5A + ZP6 + CAB

    # Filtrar o DataFrame para manter apenas as linhas cujo STATUS está em all_stations
    df_tst = df_tst[df_tst['STATUS'].isin(all_stations)]
    
    # Lista de KNRs únicos no dataset
    knrs_unicos = df_tst['KNR'].unique()

    # Filtrar os KNRs que têm pelo menos uma estação de cada ZP e CAB
    knrs_validos = [knr for knr in knrs_unicos if has_at_least_one_station_from_each(df_tst, knr)]

    # Filtrar o DataFrame original para manter apenas os KNRs válidos
    df_filtered = df_tst[df_tst['KNR'].isin(knrs_validos)]
    
    df_filtered['DATA'] = pd.to_datetime(df_filtered['DATA'], errors='coerce')


    df_filtered = df_filtered.sort_values(by=['KNR', 'DATA'])
    
        # Aplicar a função de grupo ao dataframe
    df_filtered['Group'] = df_filtered['STATUS'].apply(get_group)

    # Calcular a diferença de tempo entre os status consecutivos para o mesmo KNR
    df_filtered['Tempo'] = df_filtered.groupby('KNR')['DATA'].diff().dt.total_seconds() / 60  # Diferença em minutos

    # Preencher NaN com 0, já que a primeira ocorrência não tem tempo anterior
    df_filtered['Tempo'] = df_filtered['Tempo'].fillna(0)

    # Criar colunas para armazenar o tempo gasto em cada ZP/CAB
    for group in station_to_group.keys():
        df_filtered[f'Tempo_{group}'] = df_filtered.apply(lambda row: row['Tempo'] if row['Group'] == group else 0, axis=1)

    # Agrupar por KNR e somar o tempo gasto em cada ZP/CAB
    df_result = df_filtered.groupby('KNR').agg({f'Tempo_{group}': 'sum' for group in station_to_group.keys()}).reset_index()   
    
    return df_result

```

Aqui temos um processamento maior dos dados de status. Primeiro, dropamos as colunas que não são necessárias, filtramos as linhas onde a coluna STATUS não é nula, transformamos a coluna DATA para datetime, filtramos as linhas onde o STATUS está em all_stations, filtramos os KNRs que têm pelo menos uma estação de cada ZP e CAB, ordenamos o DataFrame por KNR e DATA, aplicamos a função de grupo ao dataframe, calculamos a diferença de tempo entre os status consecutivos para o mesmo KNR, preenchemos NaN com 0, criamos colunas para armazenar o tempo gasto em cada ZP/CAB, agrupamos por KNR e somamos o tempo gasto em cada ZP/CAB.

## Juntamos com ultimo dados com os dados do datalake

Depois de processar os dados de resultados, falhas e status, juntamos com os dados do datalake. Para isso, pegamos os dados do datalake, transformamos em DataFrame e juntamos com os dados processados.

## Salvar os dados no datalake

Por fim, salvamos os dados processados no datalake. Para isso, transformamos o DataFrame em um arquivo CSV e salvamos no datalake.

## Treinamento do modelo

Com os dados processados salvos no datalake, podemos treinar o modelo. Para isso, pegamos os dados do datalake, a partir do nome que criamos para ele, transformamos em DataFrame e treinamos o modelo. Segue o código:

```python

async def retrainModel(name_file: str):
    try:
        
        file_content = await download_file_warehouse(name_file)
            
        # Tranformar em um dataframe
        
        df = pd.read_csv(file_content['content'])
        
        # Selecionar apenas as colunas numéricas para normalização
        colunas_numericas = df.select_dtypes(include=['float64', 'int64']).columns

        # Instanciar o MinMaxScaler
        scaler = MinMaxScaler()

        # Aplicar o scaler para as colunas numéricas
        df[colunas_numericas] = scaler.fit_transform(df[colunas_numericas])
    
        # Converter as colunas SomaTempo1, SomaTempo2 e SomaTempo718 para o tipo time delta
        df['SomaTempo1'] = pd.to_timedelta(df['SomaTempo1'])
        df['SomaTempo2'] = pd.to_timedelta(df['SomaTempo2'])
        df['SomaTempo718'] = pd.to_timedelta(df['SomaTempo718'])
        
        df['SomaTempo1'] = df['SomaTempo1'].dt.total_seconds()
        df['SomaTempo2'] = df['SomaTempo2'].dt.total_seconds()
        df['SomaTempo718'] = df['SomaTempo718'].dt.total_seconds()
        
        X = df[['Nvezes1', 'Nvezes2', 'Nvezes718', 'SomaTempo1', 'SomaTempo2', 'SomaTempo718', 'TemFalhaRod']].values

        Y = df['TemFalhaRod'].values
        
        X = np.expand_dims(X, axis=1)
        
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
        
        model = Sequential()
        model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=False))
        model.add(Dropout(0.2))
        model.add(Dense(units=1, activation='sigmoid'))
        
        
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        # Treinando o modelo
        model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)
        
        loss, accuracy = model.evaluate(X_test, y_test)
        print(f'Test Accuracy: {accuracy:.2f}')
        
        # Salvar o modelo
        model.save('model.h5')
        
        # Formatar o nome do modelo com a data
        model_name = f'model_{datetime.now().strftime("%Y-%m-%d")}'
        
        model_data = ModelTraining(model_name=model_name, training_accuracy=accuracy, date=datetime.now().strftime("%Y-%m-%d"))
        
        await insert_model(model_data)
        
        # Salvar os dados no datalake
        await upload_file(csv_file)
        
        return {"message": "Modelo treinado com sucesso"}
    
    except Exception as e:
        return {"message": f"Erro ao treinar o modelo: {str(e)}"}

```

Após isso salvamos o modelo no datalake e as métricas do treinamento no banco de dados.



[1] O que é ETL?. Oracle. Disponível em: https://www.oracle.com/br/integration/what-is-etl/. Acesso em: 28 set. 2024.