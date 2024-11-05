from pymongo import MongoClient
import gridfs
from fastapi import UploadFile, HTTPException

# Conectar ao pc do Lab
client = MongoClient("mongodb://3.84.220.52:27017/")
db = client["data_warehouse"]  # Nome do banco de dados
fs = gridfs.GridFS(db)

async def upload_file_warehouse(file_content, new_filename: str):
    try:
        file_id = fs.put(file_content, filename=new_filename)
        return {"message": "Arquivo carregado com sucesso!", "file_id": str(file_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao carregar o arquivo: {str(e)}")

async def download_file_warehouse(filename: str):
    file_data = fs.find_one({"filename": filename})
    if not file_data:
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")
    return {"filename": filename, "content": file_data.read().decode("utf-8")}

async def list_files_warehouse():
    files = []
    for file in fs.find():
        files.append({
            "filename": file.filename,
            "file_id": str(file._id),
            "size": file.length,
        })
    return {"files": files}

async def list_databases():
    databases = client.list_database_names()
    return {"databases": databases}
