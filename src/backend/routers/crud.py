from fastapi import APIRouter
from controllers.banco.supabase import create_supabase_client
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()
supabase = create_supabase_client()

class ModelTraining(BaseModel):
    model_name: str
    training_accuracy: float
    date: str 
    atual: bool = False

@router.post("/insert_model_training")
def insert_model(input_data: ModelTraining):
    # Converte a string da data para o formato datetime
    try:
        date_formatted = datetime.strptime(input_data.date, "%Y-%m-%d")
    except ValueError:
        return {"message": "Data inválida. O formato correto é YYYY-MM-DD"}

    # Converte a data para uma string antes de inserir
    date_as_string = date_formatted.strftime("%Y-%m-%d %H:%M:%S")

    # Obtem o modelo anterior para comparação
    previous_model = supabase.from_("model_training")\
        .select("*")\
        .order("date", desc=True)\
        .limit(1)\
        .execute()

    # Verifica se um modelo anterior foi encontrado
    if previous_model.data:
        previous_accuracy = previous_model.data[0]["training_accuracy"]
        comparison_result = (
            "Melhoria" if input_data.training_accuracy > previous_accuracy else "Piorou"
        )
    else:
        comparison_result = "Primeiro modelo"

    # Insere o novo modelo no banco de dados
    new_model = supabase.from_("model_training")\
        .insert({
            "model_name": input_data.model_name,
            "training_accuracy": input_data.training_accuracy,
            "date": date_as_string,
            "atual": input_data.atual
        })\
        .execute()

    # Verifica se o novo modelo foi inserido com sucesso
    if new_model.data:
        return {
            "message": "Model created successfully",
            "comparison_with_previous": comparison_result,
        }
    else:
        return {"message": "Model creation failed"}

@router.get("/model_training_history")
def get_model_training_history():
    # Recupera o histórico de treinamento dos modelos
    training_history = supabase.from_("model_training")\
        .select("*")\
        .order("date", desc=True)\
        .execute()

    if training_history.data:
        return {"training_history": training_history.data}
    else:
        return {"message": "No training history found"}

class NewEntries(BaseModel):
    date: datetime
    nvezes1: int
    nvezes2: int
    nvezes718: int
    somatempo1: int
    somatempo2: int
    somatempo718: int


@router.post("/insert_data_entries")
def insert_data_entries(input_data: NewEntries):
    
    print(input_data)
    
    # Converte a data para uma string antes de inserir
    date_as_string = input_data.date.strftime("%Y-%m-%d %H:%M:%S")

    # Insere os novos dados no banco de dados
    new_data = supabase.from_("data_entries")\
        .insert({
            "date": date_as_string,
            "nvezes1": input_data.nvezes1,
            "nvezes2": input_data.nvezes2,
            "nvezes718": input_data.nvezes718,
            "somatempo1": input_data.somatempo1,
            "somatempo2": input_data.somatempo2,
            "somatempo718": input_data.somatempo718
        })\
        .execute()

    # Verifica se os novos dados foram inseridos com sucesso
    if new_data.data:
        return {"message": "Data entries created successfully"}
    else:
        return {"message": "Data entries creation failed"}

class PredictionResults(BaseModel):
    data_entry_id: int
    result_value: int
    date: datetime
    model_id: int


@router.post("/insert_prediciton_results")
def insert_prediction_results(input_data: PredictionResults):
    
    print(input_data)
    
    # Converte a data para uma string antes de inserir
    date_as_string = input_data.date.strftime("%Y-%m-%d %H:%M:%S")

    # Insere os resultados da predição no banco de dados
    new_results = supabase.from_("prediction_results")\
        .insert({
            "data_entry_id": input_data.data_entry_id,
            "result_value": input_data.result_value,
            "date": date_as_string,
            "model_id": input_data.model_id
        })\
        .execute()

    # Verifica se os resultados da predição foram inseridos com sucesso
    if new_results.data:
        return {"message": "Prediction results created successfully"}
    else:
        return {"message": "Prediction results creation failed"}
    
    