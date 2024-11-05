from pymongo import MongoClient
import gridfs

# Conectar ao servidor MongoDB
client = MongoClient("mongodb://10.32.0.12:27017/")

# Nome do banco de dados
db = client["data_lake"]  # Substitua pelo nome do seu banco de dados

# Inicializar o GridFS
fs = gridfs.GridFS(db)

# Listar todos os arquivos no GridFS
print("Arquivos no GridFS:")
for file in fs.find():
    print(f"Nome: {file.filename}, ID: {file._id}, Tamanho: {file.length} bytes")
