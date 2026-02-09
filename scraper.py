import pandas as pd
import requests
import time
from bs4 import BeautifulSoup





headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"}

book_details = []
book_boxes = []
amount_of_books = 0
for i in range(1,4):
    site_url = f"https://books.toscrape.com/catalogue/page-{i}.html"


    print(f"Scraping Page {i}")
    site = requests.get(site_url, headers=headers)


    if site.status_code != 200:
        print("Error Accessing Website")
        break
        
    else:
        soup = BeautifulSoup(site.text, 'html.parser')

        
        book_boxes = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
        

        amount_of_books += len(book_boxes)
        

        

        for book in book_boxes:
            if book.find("div", class_="product_price"):
                price = book.find("div", class_="product_price").p.text
            else:
                price = "price Missing"
            

            if book.a.img['alt']:
                name =  book.a.img['alt']
            else:
                name = "Name Missing"

            if book.a['href']:
                link = "https://books.toscrape.com/" + book.a['href']
            else:
                link = "Link Missing"
            
            
            book_details.append({"name":name,
                                    "price": price,
                                    "product_link": link})
    time.sleep(1)


print("Scraped "+ str(amount_of_books)+" books")
print("Extracted Books from the site!")
data = pd.DataFrame(book_details)
data.to_csv("books.csv")
data.to_excel("books.xlsx", index=False)
print("Books saved to the Files")

            