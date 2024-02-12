import pandas as pd
from pymongo import MongoClient

# Configura la conexión a MongoDB Atlas
client = MongoClient("mongodb+srv://jose:1234@bs2.phmixfa.mongodb.net/")
db = client["lab3"]
collection = db["data"]

# Carga el archivo CSV en un DataFrame de pandas
data = pd.read_csv("larger_sales_dataset.csv")

# Convierte el DataFrame a un formato adecuado para MongoDB y inserta los datos
data_dict = data.to_dict(orient='records')
collection.insert_many(data_dict)
