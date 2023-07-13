# from dotenv import dotenv_values

# config = dotenv_values(".env")  # config = {'DOMAIN': 'example.org', 'ADMIN_EMAIL': 'admin@example.org', 'ROOT_URL': 'example.org/app'}


# import os
# from dotenv import load_dotenv

# load_dotenv()

# Username = os.getenv('Paulius')
# Password = os.getenv('Password')


# def check_logins(username_input: str, password_input: str):
#     username_input = input('Enter username: ')
#     password_input = input('Enter password: ')
#     if username_input == Username and password_input == Password:
#         return "Access granted"


# # check_logins('Paulius', 'Password')
# import os


# from dotenv import dotenv_values

# # Read username and password from .env file
# config = dotenv_values("credentials.env")
# username = config["username"]
# password = config["password"]

# while True:
#     # Prompt user to enter their credentials
#     user_input_username = input("Enter your username: ")
#     user_input_password = input("Enter your password: ")

#     # Check if credentials are correct
#     if user_input_username == username and user_input_password == password:
#         print("ACCESS GRANTED")
#         break
#     else:
#         print("WRONG CREDENTIALS")




# def digit_difference(num):

#     str_num = str(num)


#     digits = [int(d) for d in str_num]


#     ascending_digits = sorted(digits)
#     descending_digits = sorted(digits, reverse=True)


#     smallest_num = int("".join(str(d) for d in ascending_digits))
#     largest_num = int("".join(str(d) for d in descending_digits))


#     diff = largest_num - smallest_num


#     return diff

# num = 112
# result = digit_difference(num)
# print(result) 



# from typing import List
#veikia tik su vienu nuliu jei ivesta


def decode_string(encoded_string: str) -> str:


    parts = encoded_string.split("0")
    print(parts)



    first_name = parts[0]
    last_name = parts[1]
    id_number = int(''.join(filter(str.isdigit, parts[2])))
    

    decoded_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "id": id_number
    }
    
    return decoded_dict



encoded_string = "Paulius00Antanas0123"
decoded_dict = decode_string(encoded_string)
print(decoded_dict)
