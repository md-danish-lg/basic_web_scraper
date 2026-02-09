
# Multi-Page Web Scraper 

## 📌 Overview

This Python tool is a production-like web scraper that extracts product listings from a multi-page website and exports the collected data into CSV and Excel files. I

## 🚀 Features

* Scrapes data from multiple pages automatically
* Uses browser-like headers to reduce blocking
* Handles missing fields 
* Implements polite rate limiting with delays
* Extracts structured product data
* Exports results to:

  * CSV (.csv)
  * Excel (.xlsx)
* Console logging for progress tracking

## 🛠 Technologies Used

* Python
* requests
* BeautifulSoup4
* pandas
* lxml

## 📦 Installation

1. Clone or download this repository
2. (Recommended) Create and activate a virtual environment
3. Install dependencies:

```
pip install requests beautifulsoup4 lxml pandas openpyxl
```

## ▶️ How to Run

Run the scraper with:

```
python scraper.py
```

## 📄 Output

After execution, the script will generate:

* books.csv
* books.xlsx

Each file contains:

* Book Name
* Price
* Product Link

## 🌐 Target Website

This project is configured to scrape:

[https://books.toscrape.com](https://books.toscrape.com)

The scraper automatically navigates through multiple pages and combines all results into a single dataset.

## 🧩 Use Cases

* Product price monitoring
* E-commerce data collection
* Market research
* Building datasets for analysis
* Lead and listing extraction
* Client data scraping jobs

## ⚙️ Key Scraping Techniques Implemented

* Pagination handling
* Custom User-Agent headers
* Rate limiting (time delays)
* Nested HTML parsing
* Relative to absolute URL conversion
* Missing field handling

## ⚠️ Notes

* This project is for educational and portfolio purposes
* Always respect a website’s Terms of Service and robots.txt
* Increase delays for larger websites to avoid blocking
* Structure can be reused for client projects on similar sites

