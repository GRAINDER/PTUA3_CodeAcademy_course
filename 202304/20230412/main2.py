# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find('div', class_ = 'headline')
# print(blokas.prettify())



# from bs4 import BeautifulSoup
# import requests

# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')

# for blokas in blokai:
#     try:
#         kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#         tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#         linkas = blokas.find('a', class_="CBarticleTitle")['href']
#         print(kategorija)
#         print(tekstas)
#         print(linkas)
#     except:
#         pass





from bs4 import BeautifulSoup
import requests
import csv
import re

source = requests.get('https://www.delfi.lt/').text

soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('div', class_=re.compile(r'col-xs-.'))

with open("delfi_naujienos.csv", 'w', encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['KATEGORIJA', 'ANTRAŠTĖ', 'NUORODA'])

    for blokas in blokai:
        try:
            kategorija = blokas.find("div", class_='headline-category').text.strip()
            tekstas = blokas.find('a', class_="CBarticleTitle").text.strip()
            linkas = blokas.find('a', class_="CBarticleTitle")['href']
            print(kategorija, tekstas, linkas)
            csv_writer.writerow([kategorija, tekstas, linkas])
        except:
            pass