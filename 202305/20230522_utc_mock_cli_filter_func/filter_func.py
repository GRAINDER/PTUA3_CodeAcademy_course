from typing import List
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["random_db"]
collection = db["random_db"]

# Filtering using $eq operator
def filter_by_equals(field_name: str, value: str) -> List[dict]:
    query = {field_name: {"$eq": value}}
    result = collection.find(query)
    return list(result)

# Example usage: Filter documents where the "age" field is equal to 25
filtered_equals = filter_by_equals("Name", "VBnJPzoS")
print(filtered_equals)


# Filtering using $ne operator
def filter_by_not_equals(field_name: str, value: str) -> List[dict]:
    query = {field_name: {"$ne": value}}
    result = collection.find(query)
    return list(result)

# Example usage: Filter documents where the "name" field is not equal to "John"
filtered_not_equals = filter_by_not_equals("Name", "VBnJPzoS")
print(filtered_not_equals)
