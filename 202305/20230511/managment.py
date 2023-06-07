from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Dict, Any, List
from bson.objectid import ObjectId

class LibraryManager:
    def __init__(self, host: str, port: int, db_name: str, collection_name: str):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_book(self, book: Dict[str, Any]) -> str:
        result = self.collection.insert_one(book)
        return str(result.inserted_id)

    def get_all_books(self) -> List[Dict[str, Any]]:
        return list(self.collection.find())

    def get_book(self, book_id: str) -> Dict[str, Any]:
        return self.collection.find_one({"_id": ObjectId(book_id)})

    def update_book(self, book_id: str, updates: Dict[str, Any]) -> bool:
        result = self.collection.update_one({"_id": book_id}, {"$set": updates})
        return result.modified_count > 0

    def delete_book(self, book_id: str) -> bool:
        result = self.collection.delete_one({"_id": book_id})
        return result.deleted_count > 0


my_book = LibraryManager(host="localhost", port=27017, db_name="books", collection_name="science_books")
# my_book.add_book(book={"name": "Pauliaus nuotykiai"})
# print(my_book)

# my_book.update_book(book_id="_id", updates={"test": "116561adas1fdsaf1af1saf1a"})

id = "645d1c897fafa38104f624e9"

objInstance = ObjectId(id)





id = "645d1c897fafa38104f624e9"

objInstance = ObjectId(id)

print(my_book.collection.find_one({"_id": objInstance}))





