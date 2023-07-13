from pymongo import MongoClient
from pymongo.errors import ExecutionTimeout, PyMongoError

def query_with_timeout(database_name: str, collection_name: str, query: dict, timeout_ms: int) -> list:
    try:
        # Connect to MongoDB
        client: MongoClient = MongoClient('mongodb://localhost:2701')
        db = client["Warehouse"]
        collection = db["Fruits"]
        
        # Set query options with timeout
        query_options = {'$query': query, '$maxTimeMS': timeout_ms}
        
        # Perform the query
        result = list(collection.find(query_options))
        
        # Close the MongoDB connection
        client.close()
        
        return result
    
    except ExecutionTimeout as e:
        print('Query execution timeout:', str(e))
        return []
    
    except PyMongoError as e:
        print('An error occurred:', str(e))
        return []

# Usage
database_name = 'Warehouse'
collection_name = 'Fruits'
query = {"Quantity": {"$lte": 2}}
timeout_ms = 50

query_result = query_with_timeout(database_name, collection_name, query, timeout_ms)

if query_result:
    print('Query result:', query_result)
else:
    print('No results or error occurred during the query.')
