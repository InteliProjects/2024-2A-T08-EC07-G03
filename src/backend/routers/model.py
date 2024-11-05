from fastapi import APIRouter, HTTPException, UploadFile, File
from controllers.model import predict_failure, retrainModel
from controllers.datalake import upload_file
from controllers.model import process_data_datawarehouse
from pydantic import BaseModel
from datetime import datetime
from typing import List
import pandas as pd
import os

router = APIRouter()

class KNRData(BaseModel):
    knr: str

@router.post("/predict")
async def predict(input_data: KNRData):
    try:
        # Fazer a predição usando o KNR fornecido
        print(f"KNR: {input_data.knr}")
        result = await predict_failure(input_data.knr)
        
        if result is None:
            raise HTTPException(status_code=404, detail="KNR não encontrado ou predição inválida.")
        
        return {"knr": input_data.knr, "prediction": result}
    
    except ValueError as e:
        # Lançar uma exceção para KNR não encontrado
        raise HTTPException(status_code=404, detail=str(e))
    
    except Exception as e:
        # Tratar qualquer outra exceção inesperada
        raise HTTPException(status_code=500, detail=f"Erro ao fazer a predição: {str(e)}")

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

        # Chama a função de processamento dos dados
        final_file_name = await process_data_datawarehouse(resultado_names, falhas_names, status_names)

        # Chama a função de retreinamento do modelo com os dados fornecidos
        await retrainModel(final_file_name)

        if save_new_model:
            return {"detail": "Modelo retreinado e salvo com sucesso."}
        else:
            return {"detail": "Novo modelo descartado. Modelo antigo restaurado com sucesso."}

    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="Um dos arquivos CSV está vazio ou inválido.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao retreinar o modelo: {str(e)}")