# json_object = {
#     "name": "John Doe",
#     "age": 25,
#     "is_student": True,
#     "interests": ["reading", "traveling", "photography"],
#     "address": {
#         "street": "123 Main Street",
#         "city": "New York",
#         "country": {"name": "United States", "code": "US"},
#     },
#     "birth_date": "1998-05-10",
#     "metadata": {"category": "A", "priority": 1},
#     "favorite_things": ["apple", 5, False],
# }


# #answer
# validation_rules = {
#     'validator': {
#         '$jsonSchema': {
#             'bsonType': 'object',
#             'required': ['name', 'age', 'is_student', 'interests', 'address', 'city', 'birth_date', 'metadata', 'favorite_things'],
#             'properties': {
#                 "name": {'bsonType': 'string'},
#                 "age": {'bsonType': 'string'},
#                 "is_student": {'bsonType': 'bool'},
#                 'interests': {
#                     'bsonType': 'object',
#                     'required': ['interest_one', 'interest_two', 'interest_three'],
#                     'properties': {
#                         'interest_one': {'bsonType': 'string'},
#                         'interest_two': {'bsonType': 'string'},
#                         'interest_three': {'bsonType': 'string', 'bsonType': 'string'},
#                 'address':{
#                     'bsonType': 'object',
#                     'required': ['street', 'city', 'country'],
#                     'properties': {
#                         'street': {'bsonType': 'string'},
#                         'city': {'bsonType': 'string'},
#                         'country': {'bsonType': 'string'},
#                 'birth_date': {'bsonType': 'string'},
#                 'metadata': {'bsonType': 'string', 'bsonType': 'int', 'minimum': 0},
#                 'favorite_things': {'bsonType': 'int', 'pattern': bool},
#                             }
#                         }
#                     }
#                 }
#             }
#         }
#     }
# }






validation_rules = {
    'validator': {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['person', 'products'],
            'properties': {
                "name": {'bsonType': 'string'},
                "age": {'bsonType': 'int'},
                "is_student": bool,
                'address': {
                    'bsonType': 'object',
                    'required': ['street', 'city', 'country'],
                    'properties': {
                        'street': {'bsonType': 'string'},
                        'city': {'bsonType': 'string'},
                        'country': {'bsonType': 'string', 'bsonType': 'string'},
                'contacts':{
                    'bsonType': 'object',
                    'required': ['type', 'value'],
                    'properties': {
                        'email': {'bsonType': 'string'},
                        'phone': {'bsonType': 'string'},
                        }              
                    }
                }
            }
        }
    }
}