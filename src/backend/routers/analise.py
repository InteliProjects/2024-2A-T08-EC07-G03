from fastapi import APIRouter
from controllers.analise import (
    get_data_entries,
    get_analysis_results,
    get_model_training,
)

router = APIRouter()


@router.get("/data-entries")
async def data_entries_endpoint():
    return await get_data_entries()


@router.get("/analysis-results")
async def analysis_results_endpoint():
    return await get_analysis_results()


@router.get("/model-training")
async def model_training_endpoint():
    return await get_model_training()
