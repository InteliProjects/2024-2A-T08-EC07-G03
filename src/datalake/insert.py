from pymongo import MongoClient
import gridfs

# Conectando ao MongoDB
client = MongoClient("mongodb://10.32.0.12:27017/")
db = client["data_lake"]  # Nome do banco de dados
fs = gridfs.GridFS(db)  # Inicializa o GridFS

# Caminho para o arquivo de exemplo
file_path = "exemplo.txt"

# Carregar o arquivo no GridFS
with open(file_path, "rb") as f:
    file_id = fs.put(f, filename="exemplo.txt")  # Upload do arquivo
    print(f"Arquivo carregado com ID: {file_id}")
