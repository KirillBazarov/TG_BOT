import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017")

db = db_client["for_tg"]

collection = db["funds"]
