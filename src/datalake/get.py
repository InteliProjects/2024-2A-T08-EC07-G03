from pymongo import MongoClient
import gridfs

# Conectar ao servidor MongoDB
client = MongoClient("mongodb://44.208.228.224:27017/")

# Nome do banco de dados
db = client["data_lake"]

# Inicializar o GridFS
fs = gridfs.GridFS(db)

# Recuperar o arquivo pelo nome
file_data = fs.find_one({"filename": "exemplo.txt"})  # Substitua pelo nome do arquivo
print(file_data.read())  # Exibir o conteúdo do arquivo
