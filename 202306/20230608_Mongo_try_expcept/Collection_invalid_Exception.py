from pymongo import MongoClient
from pymongo.errors import CollectionInvalid, PyMongoError

def create_collection(database_name: str, collection_name: str) -> bool:
    try:
        # Connect to MongoDB
        client: MongoClient = MongoClient('mongodb://localhost:27017')
        db = client[database_name]
        
        # Create a collection
        db.create_collection(collection_name)
        
        # Close the MongoDB connection
        client.close()
        
        return True
    
    except CollectionInvalid as e:
        print('Collection creation error:', str(e))
        return False
    
    except PyMongoError as e:
        print('An error occurred:', str(e))
        return False

# Usage
database_name = 'Warehouse'
collection_name = 'Drinks'

if create_collection(database_name, collection_name):
    print('Collection created successfully.')
else:
    print('Failed to create collection.')
