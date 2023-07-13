
validation_rules = {
    'validator': {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['name', 'age', 'email'],
            'properties': {
                'name': {'bsonType': 'string'},
                'age': {'bsonType': 'int', 'minimum': 0},
                'email': {'bsonType': 'string', 'pattern': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'}
            }
        }
    }
}

