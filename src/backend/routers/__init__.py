from fastapi import APIRouter
from .hello import router as hello
from .model import router as model
from .crud import router as crud
from .datalake import router as datalake
from .health import router as healthCheck
from .dataWarehouse import router as dataWarehouse
from .analise import router as analise

router = APIRouter()

router.include_router(hello, prefix="/hello")
router.include_router(model, prefix="/model")
router.include_router(crud, prefix="/crud")
router.include_router(datalake, prefix="/datalake")
router.include_router(healthCheck, prefix="/healthcheck")
router.include_router(dataWarehouse, prefix="/datawarehouse")
router.include_router(analise, prefix="/analise")
