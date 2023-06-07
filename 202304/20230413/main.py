# from typing import List
# class my_list:
#     def __init__(self, items: List[int]) -> None:
#         self.items = items


# print(dir(my_list))

# my_listt = my_list(items=[1, 2, 3])
# print(bool(my_listt))


# class Product:
#     def __init__(self, name: str, price: float) -> None:
#         self.name = name
#         self.price = price

#     def __str__(self) -> str:
#         return f'Product {self.name}, Price: {self.price}'

#     def __repr__(self) -> str:
#         return f'Product {self.name, self.price}'

# my_product = Product(name = "MilkyWay", price = 1.5)
# print(str(my_product))
# print(repr(my_product))
# from typing import List, Optional

# class MyQueue:
#     def __init__(self, queue: List[Optional[int]]) -> None:
#         self.queue = queue

#     def __bool__(self) -> bool:
#         return bool(self.queue)

#     def __repr__(self) -> str:
#         return f'MyQueue {self.queue}'
    
#     def __len__(self) -> int:
#         return len(self.queue)
    

# my_queue = MyQueue(queue=[])
# print(bool(my_queue))
# print(repr(my_queue))
# print(len(my_queue))

# my_queue_two = MyQueue(queue=[1, 2, 3, 4])
# print(bool(my_queue_two))
# print(repr(my_queue_two))
# print(len(my_queue_two))




    
# from typing import List

# Image = List[List[int]] 

# def flatten_image(image: Image) -> List: 
# #custom type Image 
#     flat_list = [] 
#     for sublist in image: 
#         for item in sublist: 
#             flat_list.append(item)
#     return flat_list

# image = [[1,2,3],[4,5,6]]



# Create three different task with real world scenario what would include all magic methods we covered today and plus 3 others from the provided list.

from typing import Optional


class Patient:
    def __init__(self, age: int, name: str, surname: str, gender: str, disease: Optional[str], height: float, weight: int, bmi: float) -> None:
        self.age = age
        self.name = name
        self.surname = surname
        self.gender = gender
        self.disease = disease
        self.height = height
        self.weight = weight
        self.bmi = bmi

    
    def __str__(self) -> str:
        return f'New patient name and surname is: {self.name} {self.surname}'
    
    def __repr__(self) -> str:
        return f'Patient age: {self.age} and gender: {self.gender}'


    def __bool__(self) -> bool:
        return bool(self.disease)
    
    # def __getitem__(self) -> str:
    #     return self.disease
    

new_patient = Patient(35, "Paulius", "Dailidonis", "Male", "Overcolded", 85, 1.79, 31.5)
print(str(new_patient))
print(repr(new_patient))
print(f"Is patient sick? {bool(new_patient)}")



    
    

    
