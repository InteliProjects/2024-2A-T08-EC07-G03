from fastapi import APIRouter, UploadFile, File
from controllers.DataWarehouse.file_manager_warehouse import upload_file_warehouse, download_file_warehouse, list_files_warehouse, list_databases

router = APIRouter()

# Rota de upload de arquivo
@router.post("/upload")
async def upload_file_warehouse(file: UploadFile = File(...)):
    return await upload_file_warehouse(file)

# Rota para recuperar arquivo pelo nome
@router.get("/download/{filename}")
async def download_file_warehouse_file(filename: str):
    return await download_file_warehouse(filename)

# Rota para listar todos os arquivos
@router.get("/list")
async def list_files_warehouse_files():
    return await list_files_warehouse()

# Rota para listar todos os bancos de dados
@router.get("/databases")
async def list_database_warehouse():
    return await list_databases()


