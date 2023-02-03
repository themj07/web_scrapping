import requests
from bs4 import BeautifulSoup
import pyodbc 

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=localhost;'
                      'Database=Jumia;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

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

conn.close()
