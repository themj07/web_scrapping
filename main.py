import requests
from bs4 import BeautifulSoup
import pyodbc

url = 'https://www.jumia.ci/index/allcategories/'
BASE = "https://www.jumia.ci"
response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, 'html.parser')
Tags = []
divs = soup.find_all('div', class_="col4 -pvm -bb")
for div in divs:
    links = div.find_all('a')
    for link in links:
        Tags.append(link.text)
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost;'
                      'Database=Jumia;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
for tag_name in Tags :
    cursor.execute("INSERT INTO Tags (tag_name) VALUES (?)", tag_name)
conn.commit()


# categories

url = "https://www.jumia.ci/index/allcategories/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
categories = soup.find_all("a", class_="-pbm -m -upp -hov-or5")
for category_name in categories:
    cursor.execute("INSERT INTO categories (category_name) VALUES (?)", category_name.text)
conn.commit()
cursor.execute("SELECT * FROM categories")
for row in cursor:
    print(row)


# produit


url = 'https://www.jumia.ci/mlp-boutiques-officielles/?viewType=list'
while url:
    response = requests.get(url)
    page = response.content
    soup = BeautifulSoup(page, 'html.parser')

    divs = soup.find_all('div', class_="main")
    for div in divs:
        nom = div.find('h3', class_='name').text
        avis = div.find('div', class_='rev').text
        cursor.execute("INSERT INTO article (produit_name, avis) VALUES (?, ?)", (nom, avis))

    next_page_link = soup.find('a', attrs={'data-catalog': True})
    if next_page_link:
        url = "https://www.jumia.ci/mlp-boutiques-officielles/" + next_page_link['href']
    else:
        url = None


conn.commit()
conn.close()
