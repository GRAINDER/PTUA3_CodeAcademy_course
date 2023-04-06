# import requests

# r = requests.get('https://www.benu.lt')

# # print(r.text)
# # print(dir(r))


# # r = requests.get('https://www.python.org/static/img/python-logo.png')
# print(r.content)

# with open('logo.png', 'wb') as f:
# #     f.write(r.content)




import requests, json
# url = 'https://raw.githubusercontent.com/robotautas/kursas/master/requests/uzduotis.json'
# f = requests.get(url)
# data = f.json()
# # print(data)
# # print(type(data))





# new_data = data.update({
#   "colors": [
#     {
#       "color": "black",
#       "rgb": "255, 255, 255",
#       "hex": "#000"
#     },
#     {
#       "color": "white",
#       "rgb": "0, 0, 0",
#       "hex": "#FFF"}]
#     }
# )



# r = requests.get('http://python.org/')
# print(r.headers)


# # print(data)


# new_json = json.dumps(data, indent=2)
# print(new_json)

# import requests

# def get_servers(urls):
#     servers = []
#     for url in urls:
#         try:
#             response = requests.get(url)
#             server = response.headers['Server']
#             servers.append(server)
#         except:
#             servers.append(None)
#     return servers

# servers_info = get_servers('https://www.delfi.lt/')
# print(servers_info)




# import requests
# from urllib.parse import urlparse

# def serverio_identifikavimas(urls):
#     servers = set()
#     for url in urls:
#         parsed_url = urlparse(url)
#         server = parsed_url.netloc
#         if server:
#             response = requests.head(url)
#             if response.status_code == 200:
#                 servers.add(server)
#     return servers


# servers_info = print(serverio_identifikavimas('https://www.delfi.lt/'))



import requests
import os

def issaugoti_kates(nuotrauku_skaicius):
    if not os.path.exists('kates'):
        os.makedirs('kates')
    for i in range(nuotrauku_skaicius):
        response = requests.get('https://cataas.com/cat')
        with open(f'kates/kate{i}.jpg', 'wb') as f:
            f.write(response.content)


kates = issaugoti_kates(5)