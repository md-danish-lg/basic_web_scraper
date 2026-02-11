import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import sys
import logging




logging.basicConfig(filename="app.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



headers ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
" like Gecko) Chrome/144.0.0.0 Safari/537.36"}

book_details = []
book_boxes = []




def get_page(url, i):
    logger.info(f"Scraping Page {i}: {url}")

    site = requests.get(url, headers=headers)
    if site.status_code == 200:
        return site
    else: 
        logger.warning(f"Site Requst Failed: status -> {site.status_code}")
        return False



def get_book_boxes(soup):
    return soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')


def extract_book_basic(book, base_url):
    

    if book.a['href']:
        link = f"{base_url}/catalogue/" + book.a['href']
    else:
        link = "Link Missing"
        logger.warning(f"Link not found: {book.a['title'].text}")
        

    try:
        
        book_page = requests.get(link, headers=headers)

        if book_page.status_code != 200:
            logger.warning(f"failed to get {link}: Status -> {book_page.status_code}")
        else:
            soup = BeautifulSoup(book_page.text, 'html.parser')
            content_box = soup.find("article", class_="product_page")

            
            try:
                price = get_details(content_box, "p", "price_color", "Price").text
                name = get_details(content_box, "div","product_main", "Name" ).h1.text
                upc = get_details(content_box, "table", "table-striped", "upc").find_all("tr")[0].td.text
                in_stock = get_details(content_box, "table", "table-striped", "Availibility").find_all("tr")[5].td.text
                rating =  get_details(content_box, "p", "star-rating", "Rating")['class'][-1]
                product_description = content_box.find_all("p")[3].text

                logger.info(f"Book Extracted: {name}")
                book_details.append({"UPC Code":upc,
                            "name":name,
                            "price": price,
                            "Rating(out of Five)": rating,
                            "Availibility": in_stock,
                            "Product Description": product_description,
                            "product_link": link})
                
            except:
                logger.error("Failed to Extract book info")
    except:
        logger.warning(f"Request failed: {link}")
       
        
        
    


def scrape_pages(configuration):
    start = configuration['start_page']
    end = configuration['end_page'] + 1
    
    base_url = "https://books.toscrape.com/"
    
    amount_of_books = 0
    
    for i in range(start,end):

        site_url = f"{base_url}catalogue/page-{i}.html"
        



        site = get_page(site_url, i)
        if not site:
            continue

        if site.status_code != 200:
            logger.warning(f"Error Accessing Website: {site_url} ")
            
        else:

            soup = BeautifulSoup(site.text, 'html.parser')
            book_boxes = get_book_boxes(soup)
            amount_of_books += len(book_boxes)
            
            for book in book_boxes:  
                extract_book_basic(book, base_url)
               
                
        time.sleep(0.3)

    
    logger.info("Scraped "+ str(amount_of_books)+" books")
  
    return pd.DataFrame(book_details)


def save_data(data, output="output"):
    data['price'] = data['price'].str.strip("Â£")
    data['price'] = data['price'].astype(float)
    try:
        data.to_csv(f"{output}.csv")
        data.to_excel(f"{output}.xlsx", index=False, engine="openpyxl")
        
        logger.info("Books Saved to files")
    except:
        logger.error("Failed to Save books to files")
        


def get_details(content, tag, html_class, name, ):
    if content.find(f"{tag}", class_=f"{html_class}"):
        return content.find(f"{tag}", class_=f"{html_class}")
    else:
        return None

    




arguments = sys.argv[1:]

if len(arguments)>0:
    config = {
        "start_page": int(arguments[0]),
        "end_page":int(arguments[1]),
    }
    if len(arguments) == 3:
        output_file_name = str(arguments[2])
    else:
        output_file_name = "output"


  
    logger.info("Script Start")
    logger.info(f"Extracting Page {arguments[0]} to Page {arguments[1]} --> Output File: {output_file_name}")
    data = scrape_pages(config)

    
    save_data(data, output_file_name)
    
else:
    logger.error("ARGUMENTS NOT FOUND")



