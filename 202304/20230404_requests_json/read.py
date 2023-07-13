# import json

# {
#   "firstName": "John",
#   "lastName": "Smith",
#   "isAlive": True,
#   "age": 25,
#   "address": {
#     "streetAddress": "21 2nd Street",
#     "city": "New York",
#     "state": "NY",
#     "postalCode": "10021-3100"
#   },
#   "phoneNumbers": [
#     {
#       "type": "home",
#       "number": "212 555-1234"
#     },
#     {
#       "type": "office",
#       "number": "646 555-4567"
#     }
#   ],
#   "children": [],
#   "spouse": None
# }


# data = '''{
#   "student": [ 

#      { 
#         "id":"01", 
#         "name": "Tom", 
#         "lastname": "Price" 
#      }, 

#      { 
# #         "id":"02", 
# #         "name": "Nick", 
# #         "lastname": "Thameson" 
# #      } 
# #   ]   
# # }'''

# data_dict = json.loads(data)
# print(data_dict)
# print(type(data_dict))




# data_dict['student'][1]['name'] = 'Kyle'
# for student in data_dict['student']:
#     student.update({'gender':'male'})
# print(data_dict)




# new_json = json.dumps(data_dict, indent=2)
# print(new_json)
# print(type(new_json))


# https://github.com/robotautas/kursas/blob/master/requests/uzduotis.json



import requests
from bs4 import BeautifulSoup

url = 'https://www.meteoblue.com/lt/oro-prognozes/savait%C4%97/vilnius_lietuva_593116'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    forecast = soup.find('div', {'class': 'text--center mt0 mb0'})
    
    if forecast:
        print('Oro prognozė Vilniuje šiuo metu:', forecast.text.strip())
    else:
        print('Nepavyko rasti oro prognozės.')
else:
    print('Nepavyko prisijungti prie svetainės.')
