from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.errors import PyMongoError

client = MongoClient("mongodb://localhost:27017/")
db = client["Warehouse"]
collection = db["Fruits"]

# # Filtering using $gte operator
# def filter_by_greater_than_equal(collection: Collection, field_name: str, value: int) -> None:
#     try:
#         query = {field_name: {"$gte": value}}
#         result = collection.find(query)
#         # return list(result)
#         # Perform a quer
#             # Process the result
#         if result:
#             print('Found document:', result)
#         else:
#             print('Document not found.')

#         # Close the MongoDB connection
#         # client.close()
#     except PyMongoError as e:
#         print('An error occurred:', str(e))

# # Call the function
# filter_by_greater_than_equal()
# # Example usage: Filter documents where the "age" field is greater than or equal to 25
# filtered_greater_than_equal = filter_by_greater_than_equal(collection, "Price", 99)
# print(filtered_greater_than_equal)


# result_dict1 = {}

# for item in filtered_greater_than_equal:
#     result_dict1[item["Name"]] = item["Quantity"]


# print(result_dict1)


# # Filtering using $lte operator
# def filter_by_less_than_equal(collection: Collection, field_name: str, value: int) -> List[dict]:
#     query = {field_name: {"$lte": value}}
#     result = collection.find(query)
#     return list(result)

# # Example usage: Filter documents where the "rating" field is less than or equal to 4.5
# filtered_less_than_equal = filter_by_less_than_equal(collection, "Time", 1678574589)
# print(filtered_less_than_equal)


# result_dict2 = {}

# for item in filtered_less_than_equal:
#     result_dict2[item["Name"]] = item["Quantity"]


##############################################

# 1st part
# Filtering using $lte operator for two columns and returning other two different columns
# def filter_by_less_than_equal(collection: Collection, field_quantity: str, value_one: int, field_price: str, value_two: int) -> List[dict]:
#     query = {field_quantity: {"$lte": value_one}, field_price: {"$lte": value_two}}
#     result = collection.find(query)
#     return list(result)


# filtered_less_than_equal = filter_by_less_than_equal(collection, "Quantity", 10, "Price", 20.00 )


# result_dict_one = {}

# for item in filtered_less_than_equal:
#     result_dict_one[item["Name"]] = item["Validation"]


# print(result_dict_one)


# #2nd part
# filtered_less_than_equal_and_average = filter_by_less_than_equal(collection, "Quantity", 10, "Price", 20.00 )

# amount = len(filtered_less_than_equal_and_average)

# result = 0
# for items in filtered_less_than_equal_and_average:
#     result += items["Price"]

# average = round((result / amount), 2)
# print(f"the average price per unit for those retrieved is: {average}")


# #3rd part


# # Filtering using $in operator
# def filter_by_in(collection: Collection, field_name: str, values: List[str]) -> List[dict]:
#     query = {field_name: {"$in": values}}
#     result = collection.find(query)
#     return list(result)

# #Filter fruits where  "quantity" field is in a list of quantity (5 10 15)
# quantity = [5, 10, 15]
# filtered_in = filter_by_in(collection, "Quantity", quantity)
# print(filtered_in)


# @mock.patch("pymongo.collection.Collection.find")
# def test_name(self, mock_find):
#     mock_find.return_value =  {'name' : 'Kelly', 'email' : 'kelly@gmail.com'}# rest of test


# def query_database() -> None:
#     try:
#         # Connect to MongoDB
#         client = MongoClient('mongodb://localhost:27017')
#         db = client['Warehouse']
#         collection = db['Fruits']

#         # Perform a query
#         result = collection.find_one({'Name': 'weaknesses'})

#         # Process the result
#         if result:
#             print('Found document:', result)
#         else:
#             print('Document not found.')

#         # Close the MongoDB connection
#         # client.close()

#     except PyMongoError as e:
#         print('An error occurred:', str(e))


# # Call the function
# query_database()


# from pymongo import MongoClient
# from pymongo.errors import CollectionInvalid, PyMongoError

# def create_collection(database_name: str, collection_name: str) -> bool:
#     try:
#         # Connect to MongoDB
#         client: MongoClient = MongoClient('mongodb://localhost:27017')
#         db = client["Warehouse"]
        
#         # Create a collection
#         db.create_collection("Fruits")
        
#         # Close the MongoDB connection
#         client.close()
        
#         return True
    
#     except CollectionInvalid as e:
#         print('Collection creation error:', str(e))
#         return False
    
#     except PyMongoError as e:
#         print('An error occurred:', str(e))
#         return False

# # Usage
# database_name = 'Warehouse'
# collection_name = 'Fruits'

# if create_collection(database_name, collection_name):
#     print('Collection created successfully.')
# else:
#     print('Failed to create collection.')




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
