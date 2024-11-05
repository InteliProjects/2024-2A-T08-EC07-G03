from pymongo import MongoClient
import gridfs
from fastapi import UploadFile, HTTPException

# Conectar ao pc do Lab
client = MongoClient("mongodb://3.84.220.52:27017/")
db = client["data_lake"]  # Nome do banco de dados
fs = gridfs.GridFS(db)

async def upload_file(file: UploadFile, new_filename: str):
    try:
        file_id = fs.put(file.file, filename=new_filename)
        return {"message": "Arquivo carregado com sucesso!", "file_id": str(file_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao carregar o arquivo: {str(e)}")

async def download_file(filename: str):
    try:
    
        file_data = fs.find_one({"filename": filename})
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Houve um erro ao tentar recuperar o arquivo, {str(e)}")
    
    if not file_data:
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")
    
    if "csv" in filename:
        return {"filename": filename, "content": file_data.read().decode("utf-8")}
    else:
        return {"filename": filename, "content": file_data.read()}

# Função para listar os arquivos no sistema de arquivos
async def list_files():
    files = []
    try:
        for file in fs.find():
            files.append({
                "filename": file.filename,
                "file_id": str(file._id),
                "size": file.length,
            })
    except Exception as e:
        return {"error": str(e)}
    return files

async def list_databases():
    databases = client.list_database_names()
    return {"databases": databases}

# Apagar todos os arquivos
async def delete_all_files_datalake():
    for file in fs.find({}):
        fs.delete(file._id)
    return {"message": "Todos os arquivos foram apagados com sucesso!"}
