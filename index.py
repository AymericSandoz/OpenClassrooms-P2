
import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
import os

worbook = openpyxl.Workbook()
books_data = {}

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
nav=soup.find(class_='nav-list')
categorys_a=nav.find_all('a')
categorys_a.pop(0)


# for category in categorys_a[:4]:
#  url_page_category = category.get("href")
#  page = requests.get(f"http://books.toscrape.com/{url_page_category}")
#  soup = BeautifulSoup(page.content, 'html.parser')
#  prices=soup.find_all(class_='price_color')
#  books_in_one_category=[]
#  for price in prices:
#     books_in_one_category.append(price.string)

    
#  books_data[category.string.strip()]=books_in_one_category

for category in categorys_a[:1]:
 url_page_category = category.get("href")
 page = requests.get(f"http://books.toscrape.com/{url_page_category}")
 soup = BeautifulSoup(page.content, 'html.parser')
 products=soup.find_all('article')

 for product in products[1:4]:
  products_links=product.find('a')
  url_products_links=products_links.get("href")
  url_products_links_normpath = url_products_links.replace("../../../", "")
  page = requests.get(f"http://books.toscrape.com/catalogue/{url_products_links_normpath}")

  soup = BeautifulSoup(page.content, 'html.parser')
  price=soup.find_all('td')
  print(price)



 

#save in separate csv file
# for category in categorys_a[:4]:
#  with open(f"{category.string.strip()}-books.csv", 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile,delimiter=",")
#     writer.writerow(['catégorie', 'prix'])

#     for category, books in books_data.items():
#         for book_price in books:
#             writer.writerow([category, book_price])


#Save in a workbook

# for category in categorys_a[:4]:
#     for category, books in books_data.items():
#         category_file = worbook.create_sheet(title=category)
#         category_file.cell(row=1, column=1, value="Price")

#         row=1
#         for book_price in books:
#             category_file.cell(row=row, column=1,value=book_price)
#             row=row+1
    

directory = "C:\Users\aymbe\OneDrive\Documents\formation python OC\P2\code\excelFIle"
filename = "books.xlsx"
filepath = os.path.join(directory, filename)
worbook.save(filepath)






