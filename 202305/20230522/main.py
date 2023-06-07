import random
import string
from pymongo.database import Database
from pymongo import MongoClient


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_float(min_value: float, max_value: float):
    return random.uniform(min_value, max_value)


def generate_random_integer(min_value: int, max_value: int):
     return random.uniform(min_value, max_value)



def generate_random_document(fields):
    document = {}
    for field, field_type, min_value, max_value in fields:
        if field_type == 'string':
            document[field] = generate_random_string(random.randint(min_value, max_value))
        elif field_type == 'float':
            document[field] = generate_random_float(min_value, max_value)
        elif field_type == 'integer':
            document[field] = generate_random_integer(min_value, max_value)
    return document



def get_database() -> Database:
    client = MongoClient('mongodb://localhost:27017/')
    return client['random_db']

def populate_mongodb(database_name, collection_name, fields, num_documents):
    db = get_database()
    collection = db['Users']


    for _ in range(num_documents):
        document = generate_random_document(fields)
        collection.insert_one(document)


def main():
    database_name = input("Enter the database name: ")
    collection_name = input("Enter the collection name: ")
    num_documents = int(input("Enter the number of documents to create: "))

    fields = []
    while True:
        field_name = input("Enter the field name (or press Enter to finish): ")
        if not field_name:
            break

        field_type = input("Enter the field type (string, number, integer): ")
        min_value = float(input("Enter the minimum value: "))
        max_value = float(input("Enter the maximum value: "))

        fields.append((field_name, field_type, min_value, max_value))

    populate_mongodb(database_name, collection_name, fields, num_documents)


if __name__ == '__main__':
    main()
