from bs4 import BeautifulSoup

# html = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <title>First HTML Page</title>
# </head>
# <body>
#   <div id="first">
#     <h3 data-example="yes">hi</h3>
#     <p>more text.</p>
#   </div>
#   <ol>
#     <li class="special">This list item is special.</li>
#     <li class="special">This list item is also special.</li>
#     <li>This list item is not special.</li>
#   </ol>
#   <div data-example="yes">bye</div>
# </body>
# </html>
# # """

# # soup = BeautifulSoup(html, "html.parser")
# print(soup.find("div"))

# elements = soup.select('.special')
# for element in elements:
#   print(element.name)


# import requests
# # # response = requests.get('https://oxylabs.io/')
# # # print(response.text)


# # form_data = {'key1': 'value1', 'key2': 'value2'}
# # # response = requests.post('https://oxylabs.io/', data=form_data)
# # # print(response.text)


# import requests
# proxies={'http': 'http://user:password@pr.oxylabs.io:7777'}
# response = requests.get('https://ip.oxylabs.io/', proxies=proxies)
# print(response.text)


import requests

url = "https://oxylabs.io/blog"
response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)


# blog_titles = soup.findAll(['h3', 'h4', 'h5'])
# for title in blog_titles:
#     print(title.text)
# # Output:
# # Prints all blog tiles on the page

# blog_titles = soup.select('h3, h4, h5:not(:contains("Most popular articles"))')
# for title in blog_titles:
#     print(title.text)

# # After response = requests.get()
# from lxml import html
# tree = html.fromstring(response.text)


# blog_titles = tree.xpath('//h3 | //h4 | //h5[not(contains(text(), "Most popular articles"))]')
# for title in blog_titles:
#     print(title.text)


from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

# driver = Chrome(executable_path='/path/to/driver')


# driver.get('https://oxylabs.io/blog')


# blog_titles = driver.find_elements(By.CSS_SELECTOR, 'h3, h4, h5')
# for title in blog_titles:
#    if title.text != 'Most popular articles':
#        print(title.text)
# driver.quit() # closing the browser


# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# driver = webdriver.Firefox(executable_path='/nix/path/to/webdriver/executable')
# driver.get('https://delfi.lt')
# results = []
# other_results = []
# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll(attrs={'class': 'class'}):
#     name = a.find('a')
#     if name not in results:
#         results.append(name.text)
# for b in soup.findAll(attrs={'class': 'otherclass'}):
#     name2 = b.find('span')
#     other_results.append(name.text)
# series1 = pd.Series(results, name = 'Names')
# series2 = pd.Series(other_results, name = 'Categories')
# df = pd.DataFrame({'Names': series1, 'Categories': series2})
# df.to_csv('names.csv', index=False, encoding='utf-8')


import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('div', class_ = 'productsList__wrap')

with open("Telia Samsung telefonai.csv", "w", encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])

    for blokas in blokai:
        try:
            pavadinimas = blokas.find('a', class_ = 'mobiles-product-card__title js-open-product').text.strip()
            men_kaina = blokas.find('div', class_ = 'mobiles-product-card__price-marker').text.strip()
            kaina = blokas.find_all('div', class_ = 'mobiles-product-card__price-marker')[1].text.strip()
            print(pavadinimas, men_kaina, kaina)
            csv_writer.writerow([pavadinimas, men_kaina, kaina])
        except:
            pass