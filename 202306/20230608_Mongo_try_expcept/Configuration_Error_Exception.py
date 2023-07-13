from pymongo import MongoClient
from pymongo.errors import ConfigurationError, PyMongoError
import json

def connect_to_mongodb(config_file: str) -> MongoClient:
    try:
        # Read MongoDB configuration from file
        # Assuming the configuration file is in JSON format
        with open(config_file, 'r') as f:
            config_data = json.load(f)
        
        # Extract configuration parameters
        host = config_data.get('host', 'localhost')
        port = config_data.get('port', 27017)
        username = config_data.get('username')
        password = config_data.get('password')
        auth_source = config_data.get('auth_source')
        
        # Create a MongoDB connection string
        connection_string = f"mongodb://{username}:{password}@{host}:{port}/{auth_source}"
        
        # Connect to MongoDB
        client = MongoClient(connection_string)
        
        return client
    
    except ConfigurationError as e:
        print('Configuration error:', str(e))
        return None
    
    except PyMongoError as e:
        print('An error occurred:', str(e))
        return None

# Usage
config_file = 'mongodb_config.json'

client = connect_to_mongodb(config_file)

if client is not None:
    # Perform database operations using the client object
    # ...
    print('Connected to MongoDB successfully.')
else:
    print('Failed to connect to MongoDB.')
