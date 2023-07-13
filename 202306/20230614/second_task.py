json_object = {
    "person": {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "address": {
            "street": "456 Elm Street",
            "city": "San Francisco",
            "country": {"name": "United States", "code": "US"},
        },
        "contacts": [
            {"type": "email", "value": "john.doe@example.com"},
            {"type": "phone", "value": "1 123-456-7890"},
        ],
        "education": [
            {
                "institution": "University of XYZ",
                "degree": "Bachelor's",
                "major": "Computer Science",
                "completed": True,
            },
            {
                "institution": "ABC College",
                "degree": "Master's",
                "major": "Data Science",
                "completed": False,
            },
        ],
    },
    "products": [
        {"id": 1, "name": "Product 1", "price": 19.99, "is_available": True},
        {"id": 2, "name": "Product 2", "price": 29.99, "is_available": False},
    ],
}
