---
title: Retreino e Pipeline
sidebar_position: 2
description : Lógica do pipeline de retreino desenvolvido na sprint 4
---

# Introdução

&emsp;&emsp;Dentro de toda a concepção existente no sistema deste projeto, uma das etapas mais importantes é a de retreino do modelo. Ela consiste em treinar novamente o modelo após a adição de novos dados, e dessa forma, proporcionar novas estratégias de aprendizado com base nos dados mais recentes e melhorar os resultados do modelo cada vez mais. 

&emsp;&emsp;O fluxo de retreino foi pensado levando em consideração duas personas principais do sistema, o operador e o engenheiro de dados. Para ilustrar esse fluxo, foram utilizados diagramas de blocos, que oferecem uma representação visual de um sistema ou processo. Esses diagramas utilizam blocos para simbolizar diferentes componentes ou etapas, conectados por linhas que indicam a relação entre eles, facilitando uma visão clara e organizada da estrutura do sistema. Esta abordagem é amplamente usada em áreas como engenharia, informática e matemática, entre outras, sendo uma ferramenta eficaz para simplificar informações complexas.

<p align="center"><b> Figura 1 - Fluxo de retreino</b></p>
<div align="center" class="zoom-image">
  <img src={require('../../../../static/img/fluxoRetreino.jpg').default} alt="fluxo retreino"/>
  <p><b>Fonte:</b> Elaborado pelo grupo Käfer</p>
</div>

&emsp;&emsp;O fluxo de retreinamento acima descreve se forma objetiva todo o processo, mas vale detalhar cada etapa e determinar a sua importância. O processo se inicia com o usuário na tela de treinar o modelo, em que é disponibilizada uma opção para adicionar um arquivo .csv para treinar o modelo. Após essa adição, os dados novos inseridos pelo novo arquivo serão juntados aos dados antigos, que estavam no datalake. 

&emsp;&emsp;Após essa junção, o modelo é retreinado e os resultados são mostrados em seguida. Esses resultados se referem tanto ao novo modelo recém treinado quanto ao modelo antigo antes do novo treinamento. Com ambos sendo exibidos, o usuário deve escolher entre qual dos dois modelos para seguir com a execução do modelo, para assim ser encaminhado para a tela de execução. Finalmente, após escolher um modelo de fato, ele é direicionado para a tela de execução do modelo, e o modelo escolhido é salvo no datalake.

# Pipeline

&emsp;&emsp;Uma pipeline no contexto de machine learning refere-se à automação de todo o fluxo de trabalho necessário para treinar e atualizar um modelo preditivo. Isso inclui o retreinamento do modelo, que pode ser realizado utilizando todos os dados disponíveis ou de forma incremental, com a adição de novos dados conforme necessário. O retreinamento incremental é útil para modelos que precisam ser atualizados com frequência, permitindo que novas informações sejam integradas sem a necessidade de reprocessar todo o conjunto de dados. A forma como o processo é implementado depende do projeto e do fluxo definido para o modelo, garantindo que cada etapa seja realizada de maneira eficiente e sem interrupções.

&emsp;&emsp;Além do retreinamento, uma parte crucial da pipeline é a gestão dos modelos gerados. Isso envolve a definição de como os modelos devem ser armazenados e de como as versões mais recentes podem substituir o modelo em produção. Um bom gerenciamento de modelos garante que o modelo mais atualizado seja utilizado para fazer previsões, sem comprometer a integridade do sistema, buscando assegurar que os modelos sejam constantemente aprimorados e que novas versões possam ser implementadas de forma transparente e controlada. 

&emsp;&emsp;Seguindo estes princípios, a pipeline deste projeto foi desenvolvida para permitir o funcionamento do processo de retreinamento do modelo. Dentre todo este desenvolvimento, cabe destacar algumas etapas:

## Router de retreino

&emsp;&emsp;A router de retreino é uma rota criada dentro da aplicação FastAPI, responsável por realizar o retreinamento de um modelo preditivo a partir de novos dados que são fornecidos pelo usuário. Esta rota também oferece uma opção para salvar o novo modelo ou restaurar o modelo anterior, permitindo uma escolha flexível do usuário após o retreinamento.

&emsp;&emsp;Para mostrar o funcionamento do router de treino presente na solução, segue este trecho do código:

```python
@router.post("/retrain")
async def retrain(
    resultados: List[UploadFile] = File(...),
    falhas: List[UploadFile] = File(...),
    status: List[UploadFile] = File(...),
    save_new_model: bool = True
):
    try:
        # Listas para guardar os nomes dos arquivos de cada tipo
        resultado_names = []
        falhas_names = []
        status_names = []

        # Renomear e processar os arquivos de resultado
        for resultado in resultados:
            name_file = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_resultado_{resultado.filename}'
            await upload_file(resultado, name_file)  # Subir arquivo no Data Lake (simulação)
            resultado_names.append(name_file)
```
&emsp;&emsp;Nesse trecho da rota, é processada parte da função de retreino, em que algumas variáveis como a resultados, falhas e status são definidas e configuradas perante os dados que serão adicionados, e mostra um "for" do processamento dos arquivos de resultados. O código completo pode ser visto na pasta **src/backend** deste repositório

## Controler de lógica para o processamento dos dados

&emsp;&emsp;Para implementar toda a lógica de processamento desse projeto, foi feito o processamento dos dados que é responsável por controlar a lógica de decisão sobre o que fazer com o novo modelo treinado. Dependendo da escolha do usuário, ele salva o novo modelo no lugar do antigo ou descarta o novo e restaura o modelo anterior. Dessa forma, ele gerencia tanto o processamento dos dados quanto a atualização do modelo preditivo de forma flexível e controlada, o que é fundamental para o funcionamento do nosso projeto.

## Junção dos dados

&emsp;&emsp;O controller da junção dos dados nessa solução é responsável por gerenciar o processo de combinar os novos dados do arquivo CSV com o data lake existente no projeto. Sua principal função é garantir que os dados fornecidos pelo usuário, através de um arquivo CSV, sejam integrados de forma correta e eficiente aos dados antigos, permitindo o retreinamento do modelo com um conjunto de dados atualizado.

&emsp;&emsp;Segue um trecho do código da junção apenas dos dataframes de resultados, para exemplificar o processo existente no nosso projeto:

```python
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
```

&emsp;&emsp;O controller adiciona novos dados ao data lake, formando um único conjunto de dados que será usado no retreinamento. Assim, ele assegura que o modelo seja sempre atualizado com informações relevantes, o que é essencial dado o contexto do nosso projeto. O código inteiro pode ser visto na pasta src/backend deste repositório

## Retreino com novos dados

&emsp;&emsp;O retreino do modelo com os novos dados é a etapa onde o modelo preditivo é atualizado para aprender com as novas informações adicionadas. Após a junção dos novos dados ao data lake, o conjunto completo de dados é utilizado para ajustar novamente os parâmetros do modelo, melhorando sua capacidade de fazer previsões com base nas novas tendências ou padrões encontrados.

&emsp;&emsp;Durante o retreino do modelo, o pipeline usa o mesmo algoritmo e processo de aprendizado que foi utilizado inicialmente (LSTM), mas com um volume de dados maior. Esse processo é importante para manter a precisão do modelo ao longo do tempo, garantindo que ele continue relevante e eficaz ao lidar com mudanças no comportamento dos dados ou no ambiente em que está sendo aplicado.

## Salvamento dos dados e do modelo no datalake

&emsp;&emsp;Por fim, o salvamento dos dados e do modelo no data lake é uma etapa importante para garantir que tanto os dados novos quanto o modelo atualizado sejam armazenados de forma adequada. Após o retreinamento, os novos dados provenientes do arquivo CSV são combinados com o data lake existente, garantindo que todos os dados históricos e recém-adicionados fiquem centralizados para futuros treinamentos e consultas.

&emsp;&emsp;Além disso, o salvamento do modelo treinado no data lake permite que a versão atualizada do modelo fique disponível para ser utilizada nas previsões futuras. Se o usuário optar por salvar o novo modelo, ele substitui o modelo antigo no armazenamento. Caso contrário, o modelo anterior é restaurado, mantendo a flexibilidade de usar a versão mais confiável. Isso ajuda a manter um histórico atualizado e centralizado de dados e modelos, essencial para garantir a continuidade e melhoria do sistema de predições.

[1] DIAGRAMA DE BLOCOS: CONCEITO E APLICAÇÃO
. Jdevtreinamento. Disponível em: https://www.jdevtreinamento.com.br/diagrama-de-blocos-conceito-e-aplicacao/. Acesso em: 28 set. 2024.
