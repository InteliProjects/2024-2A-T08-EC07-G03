from fastapi import HTTPException
from keras.models import load_model
import pandas as pd
from joblib import load
from controllers.banco.supabase import create_supabase_client  # Para salvar no banco
from controllers.data_process.data_process import build_feature_prediction
import os
import numpy as np

# Carregar o modelo salvo no formato .h5
model_path = os.path.abspath(os.path.join(os.getcwd(), "modelos", "modelo_final.h5"))

model = load_model(model_path)

print(type(model))
print(model)

def buscar_dados_por_knr(knr):    
    df = pd.read_excel("dados.xlsx")
    dados = df[df["KNR"] == knr]

    if dados.empty:
        raise ValueError(f"KNR {knr} não encontrado.")    

    # Selecionar as features e prepará-las para o modelo
    features = dados[
        [
            "Nvezes1",
            "Nvezes2",
            "Nvezes718",
            "SomaTempo1",
            "SomaTempo2",
            "SomaTempo718",
        ]
    ].values    

    # O Keras espera um array NumPy, então as dimensões devem estar corretas
    features = features.reshape(1, -1)

    return features

async def predict_failure(knr: str):
    # try:
    #     data = buscar_dados_por_knr(knr)
    #     print(data)
        
    #     # Fazer a predição com o modelo
    #     prediction = model.predict(data)
    #     print(type(prediction))  

    #     # Extrair o valor da predição
    #     prediction_value = int(prediction[0][0])  # Supondo que seja uma classificação binária

    #     status = "Tem falha" if prediction_value == 1 else "Não tem falha"

    #     # Salvar a predição no banco de dados
    #     supabase = create_supabase_client()
    #     supabase.from_("predictions").insert({
    #         "knr": knr,
    #         "prediction": prediction_value,
    #         "status": status,
    #     }).execute()

    #     return {"knr": knr, "prediction": prediction_value, "status": status}
    
    # except ValueError as e:
    #     raise HTTPException(status_code=404, detail=str(e))

    # Fazer a predição com o modelo Keras
    print("Chegou aqui")
    features = await build_feature_prediction(knr)
    
    print(features)
    
    # Fazer a predição de uma única amostra
    prediction = model.predict(features)
    print(f'Prediction: {prediction}')

    threshold = 0.5

    if prediction[0][0] >= threshold:
        return {"knr": knr, "prediction": float(prediction[0][0]), "status": "Tem falha"}
    else:
        return {"knr": knr, "prediction": float(prediction[0][0]), "status": "Não tem falha"}
