from pymongo import MongoClient

# Conectando ao MongoDB
client = MongoClient("mongodb://10.32.0.12:27017/")

# Listar todos os bancos de dados
databases = client.list_database_names()
print(databases)
