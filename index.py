
import requests
from bs4 import BeautifulSoup
import csv
import openpyxl
import os
import re

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

for category in categorys_a[:5]:
 url_page_category = category.get("href")
 page = requests.get(f"http://books.toscrape.com/{url_page_category}")
 soup = BeautifulSoup(page.content, 'html.parser')
 products=soup.find_all('article')
 category_file = worbook.create_sheet(title=category.string.strip())


 coloumn_headers=["product_page_url","universal_product_code","title","price_including_tax","price_excluding_tax","number_available","description","category","review_rating","image_url"]
 for col, header in enumerate(coloumn_headers, start=1):
    category_file.cell(row=1, column=col, value=header)
 
 
 row=2
 for product in products:
  
  products_links=product.find('a')
  product_page_url=products_links.get("href")
  product_page_url = product_page_url.replace("../../../", "")
  page = requests.get(f"http://books.toscrape.com/catalogue/{product_page_url}")
  soup = BeautifulSoup(page.content, 'html.parser')
  product_information=soup.find(class_='table-striped')

  td=soup.find_all('td')
  universal_product_code=td[0].string
  title=soup.find('h1').string
  price_including_tax=td[2].string
  price_excluding_tax=td[3].string
  number_available=re.search(r'\d+', td[5].string).group()
  product_description_div=soup.find(id="product_description")
  if product_description_div is not None:
    product_description = product_description_div.find_next_sibling("p").string
  else:
    product_description = "No product description available"
  review_rating=soup.find(class_="star-rating")["class"][1]

  image_div=soup.find(id="product_gallery")
  image_url=image_div.find('img')["src"]
  image_url=image_url.replace("../../", "http://books.toscrape.com/")
  
  
  coloumn_values=[product_page_url,universal_product_code,title,price_including_tax,price_excluding_tax,number_available,product_description,category.string.strip(),review_rating,image_url]
  for col, value in enumerate(coloumn_values, start=1):
   category_file.cell(row=row, column=col, value=value)
  row=row+1

# product_page_url
# ● universal_ product_code (upc)
# ● title
# ● price_including_tax
# ● price_excluding_tax
# ● number_available
# ● product_description
# ● category
# ● review_rating
# ● image_url



 

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
    

# directory = "C:\Users\aymbe\OneDrive\Documents\formation python OC\P2\code\excelFile"
# filename = "books.xlsx"
# filepath = os.path.join(directory, filename)
# worbook.save(filepath)


first_sheet = worbook['Sheet']
worbook.remove(first_sheet)
worbook.save("books.xlsx")






