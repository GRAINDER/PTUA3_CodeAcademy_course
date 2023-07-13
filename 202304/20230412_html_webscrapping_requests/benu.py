import csv

from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.benu.lt/2-uz-1-kaina").text
soup = BeautifulSoup(source, "html.parser")

blokai = soup.find_all("div", class_="bnProductCard bnProductCard--listMobile productItem productItem__wrapCount")

with open("Benu kainos.csv", "w", encoding="UTF-8", newline="") as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(["Pavadinimas", "Kaina", "Kortelės_kaina"])

    for blokas in blokai:
        try:
            pavadinimas = blokas.find("a", class_="bnProductCard__title").text.strip()
            kainos = blokas.find_all(class_ = 'money_amount')
            if len(kainos)==1:
                reguleri_kaina = kainos[0].text.strip()
                kaina_su_nuolaida = "None"
            elif len(kainos)==2:
                reguleri_kaina = kainos[1].text.strip()
                kaina_su_nuolaida = kainos[0].text.strip()

            # men_kaina = blokas.find_all(class_ = 'money_amount')[1].text.strip()
            print(pavadinimas, reguleri_kaina, kaina_su_nuolaida)
            csv_writer.writerow([pavadinimas])
        except Exception as e:
            print(e)
