from pymongo import MongoClient
from typing import List, Any
from pymongo.errors import ConnectionFailure, PyMongoError, ServerSelectionTimeoutError

class Base:
    def __init__(self) -> None:
        self.adress = None
        self.port = None
        self.database_name = None
        self.collection_name = None
    def connect_to_db(self) -> MongoClient:
        connection = f"{self.adress}:{self.port}"
        try:
            client = MongoClient(f"mongodb://{connection}",serverSelectionTimeoutMS=5000)
            client.server_info()
            return client
        except ServerSelectionTimeoutError as e:
            print("Connection failure:", str(e))
            return None
        except PyMongoError as e:
            print("An error occurred:", str(e))
            return None
        
        
x = Base()
x.adress = "127.0.0.1"
x.port = "27017"
client = x.connect_to_db()
if client is not None:
    print("Connected to MongoDB successfully.")
else:
    print("Failed to connect to MongoDB.")










