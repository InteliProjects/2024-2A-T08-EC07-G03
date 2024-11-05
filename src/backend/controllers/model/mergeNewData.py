import pandas as pd
from tensorflow.keras.models import load_model
from controllers.datalake import download_file, list_files
from controllers.DataWarehouse import upload_file_warehouse, download_file_warehouse, list_files_warehouse
from datetime import datetime
import numpy as np
import os
import shutil
from io import StringIO, BytesIO

        
# Processamento de dados cru para serem subidos no data warehouse
async def process_data_datawarehouse(resultado_names: list, falhas_names: list, status_names: list):
    
    print(resultado_names, falhas_names, status_names)
    
    df_resultados = []
    
    print(f'Processing {len(resultado_names)} files')
    
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
         
    # Merge dos dataframes de falhas
    
    df_falhas = pd.concat(df_falhas, ignore_index=True)
    
    print(df_resultado.columns)
    print(df_falhas.columns)
    
    print(df_resultado['KNR'].dtype)
    print(df_falhas['KNR'].dtype)

    
    df_resultado['temFalha'] = df_resultado['KNR'].apply(lambda knr: 1 if knr in df_falhas['KNR'].values else 0)
    
    # Processamento final
    
    df_merged = pd.merge(df_status, df_resultado, on='KNR', how='inner')
    
    df_merged = await merge_df_with_last(df_merged)
    
    # Salvar arquivo final no data warehouse
    
    # Definir o nome do arquivo final com base na data e hora atuais
    final_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_final.csv'

    # Salvar o DataFrame como CSV
    df_merged.to_csv(final_file, index=False)

    try:
        # Abrir o arquivo CSV em modo leitura binária
        with open(final_file, 'rb') as file:
            # Fazer o upload do arquivo CSV para o data warehouse
            await upload_file_warehouse(file_content=file, new_filename=final_file)

        # Opcionalmente, remover o arquivo após o upload para evitar acumulação de arquivos locais
        os.remove(final_file)
    except Exception as e:
        print(f"Erro ao salvar o arquivo no data warehouse: {str(e)}")
    
    return final_file


async def merge_df_with_last(df):
    
    # Pegar ultimo arquivo no data warehouse
    files = await list_files_warehouse()
    
    print(files)
    
    # Se tiver vazio, retornar o DataFrame original
    if not files['files']:
        return df
    else:
        last_file = files['files'][-1]['filename']
    
        # Baixar o arquivo
        file_content = await download_file_warehouse(last_file)
        
        file_content = file_content['content']
        
        df_last = pd.read_csv(StringIO(file_content))
        
        # Pegar knrs que estão no último arquivo
        knrs_last = df_last['KNR'].values
        
        # Manter apenas os KNRs que não estão no último arquivo
        df = df[~df['KNR'].isin(knrs_last)]
        
        # Merge dos dataframes
        df_final = pd.concat([df_last, df], ignore_index=True)
        
        return df_final
    
    

# FUNÇÕES PARA PROCESSAR CADA TIPO DE DADO

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

station_to_group = {
'ZP7': ['M695', 'M698', 'M701', 'M702', 'M704', 'M711', 'M712', 'M721', 'M722'],
'ZP5': ['R640', 'R650', 'R700', 'R754'],
'ZP5A': ['L534', 'L535', 'L536', 'L537', 'L538', 'L539', 'L541', 'L542', 'L543', 'L544', 'L545', 'L546', 'L547', 'L548'],
'ZP6': ['M599', 'M591', 'M592', 'M593', 'M594', 'M595', 'M596', 'M643', 'M644', 'M647', 'M648', 'M651', 'M652', 'M655', 'M656', 'M673', 'M674', 'M677', 'M678', 'M681', 'M682'],
'CAB': ['M619', 'M643', 'M644', 'M655', 'M656', 'M673', 'M674']
}

async def status_processing(df):
    
    # Processamento dos dados de status
    
    # Exibir as colunas originais
    print(df.columns)

    # Dropar as colunas que não são necessárias
    # df = df.drop(columns=['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3'])
    df.drop(['KNR',	'STATUS', 'DATA'], axis=1, inplace=True)
    
    # Transformar primeira linha em df
    df = df.iloc[1:]
    
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    
    df.columns = ['KNR', 'STATUS', 'DATA']

    # Filtrar as linhas onde a coluna STATUS não é nula
    df_tst = df.dropna(how='all')
    
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
    # df_tst = df_tst[df_tst['STATUS'].isin(all_stations)]
    
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

# Função para determinar o grupo (ZP ou CAB) baseado no STATUS
def get_group(status):

    for group, stations in station_to_group.items():
        if status in stations:
            return group
    return None

def has_at_least_one_station_from_each(df, knr):
    stations_in_knr = df[df['KNR'] == knr]['STATUS'].unique()
    
    ZP7 = ['M695', 'M698', 'M701', 'M702', 'M704', 'M711', 'M712', 'M721', 'M722']
    ZP5 = ['R640', 'R650', 'R700', 'R754']
    ZP5A = ['L534', 'L535', 'L536', 'L537', 'L538', 'L539', 'L541', 'L542', 'L543', 'L544', 'L545', 'L546', 'L547', 'L548']
    ZP6 = ['M599', 'M591', 'M592', 'M593', 'M594', 'M595', 'M596', 'M643', 'M644', 'M647', 'M648', 'M651', 'M652', 'M655', 'M656', 'M673', 'M674', 'M677', 'M678', 'M681', 'M682']
    CAB = ['M619', 'M643', 'M644', 'M655', 'M656', 'M673', 'M674']
    
    # Verifica se o KNR tem pelo menos uma estação de cada ZP e CAB
    has_zp7 = any(station in stations_in_knr for station in ZP7)
    has_zp5 = any(station in stations_in_knr for station in ZP5)
    has_zp5a = any(station in stations_in_knr for station in ZP5A)
    has_zp6 = any(station in stations_in_knr for station in ZP6)
    has_cab = any(station in stations_in_knr for station in CAB)
    
    # Retorna True se tiver pelo menos uma estação de cada grupo
    return has_zp7 and has_zp5 and has_zp5a and has_zp6 and has_cab
    
def read_excel_sheets(file):
    
    column_names = ['KNR', 'STATUS', 'DATA']  # Nomes das colunas a serem usadas

    # Carregar o arquivo Excel
    excel_data = pd.ExcelFile(file)
    
    df_list = []
    
    for i, sheet in enumerate(excel_data.sheet_names):
        print(f'Processing sheet {sheet}')
        # A primeira aba tem o cabeçalho correto
        if i == 0:
            df = pd.read_excel(excel_data, sheet_name=sheet, header=0)
        else:
            # Nas outras abas, ler os dados sem cabeçalho
            df = pd.read_excel(excel_data, sheet_name=sheet, header=None)
            # Renomear colunas para 'Unnamed: 1', 'Unnamed: 2', etc., e limpar
            df = pd.DataFrame(df[[1, 2, 3]])  # Selecionar as colunas certas
            df.columns = column_names  # Atribuir os nomes das colunas
            
        df_list.append(df)
        print(f'Processed {df.shape[0]} rows')
    
    print(f'Processed {len(df_list)} sheets')
    return pd.concat(df_list, ignore_index=True)
    