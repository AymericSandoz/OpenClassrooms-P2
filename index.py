
import requests
from bs4 import BeautifulSoup
import csv
url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

prices=[]

books_data = {}

nav=soup.find(class_='nav-list')

categorys_a=nav.find_all('a')
categorys_a.pop(0)

for category in categorys_a:

 url_page_category = category.get("href")
 page = requests.get(url)
 prices_request=soup.find_all(class_='price_color')
 books_in_one_category=[]
 for price in prices_request:
    books_in_one_category.append(price.string)

    
 books_data[category.string]=books_in_one_category
print(books_data)


with open('livres.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=",")

    writer.writerow(['catégorie', 'prix'])

    for category, books in books_data.items():
        for book_price in books:
            writer.writerow([category, book_price])








