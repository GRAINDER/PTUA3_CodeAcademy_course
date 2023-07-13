from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError
from func import filter_by_greater_than_equal

def connect_to_mongodb() -> MongoClient:
    try:
        # Connect to MongoDB
        client: MongoClient = MongoClient('mongodb://localhost:27017')
        return client
    
    except ConnectionFailure as e:
        print('Connection failure:', str(e))
        return None
    
    except PyMongoError as e:
        print('An error occurred:', str(e))
        return None

# Usage
client = connect_to_mongodb()

if client is not None:
    filter_by_greater_than_equal("Price", 99)
    print('Connected to MongoDB successfully.')
else:
    print('Failed to connect to MongoDB.')

