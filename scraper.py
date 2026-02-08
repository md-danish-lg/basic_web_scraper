import pandas as pd
import requests
from bs4 import BeautifulSoup




site = requests.get("https://books.toscrape.com/")


if site.status_code == 200:
    soup = BeautifulSoup(site.text, 'html.parser')

    book_boxes = []
    book_boxes = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    

    print("Scraped "+ str(len(book_boxes))+" books")

    book_details = []

    for book in book_boxes:
        price = book.find("div", class_="product_price")
        
        
        
        book_details.append({"name": book.a.img['alt'],
                                "price": price.p.text,
                                "product_link": "https://books.toscrape.com/" + book.a['href']})


    print("Extracted Books from the site!")
    data = pd.DataFrame(book_details)
    data.to_csv("books.csv")
    data.to_excel("books.xlsx", index=False)
    print("Books saved to the Files")
else:
    print("Error Accessing Website")