from pymongo import MongoClient
import pandas as pd

# Load data
df = pd.read_csv("People_May.csv")

# MongoDB connection
client = MongoClient("mongodb://root:example@mongo:27017/")

# Create database and collection
db = client["population"]
collection = db["people_may"]

# Insert many data
collection.insert_many(df.to_dict('records'))

# Close client
client.close()
