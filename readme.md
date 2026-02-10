# Advanced Books Scraper

A multi-page, deep web scraping project built with Python to extract detailed book data from **books.toscrape.com**. This scraper goes beyond basic list-page scraping by visiting each product page to collect rich metadata and clean it for analysis.

## 🚀 Features

* Multi-page scraping
* Deep product-page scraping
* Extracts detailed fields per book:

  * UPC Code
  * Book Name
  * Price (cleaned & converted to float)
  * Rating
  * Availability
  * Product Description
  * Product Link
* Modular, function-based architecture
* User-Agent headers + polite request delays
* Data cleaning and type conversion
* Export to CSV and Excel

## 🛠 Technologies Used

* Python 3
* requests
* BeautifulSoup4
* pandas
* openpyxl (for Excel export)

## 📂 Output Files

After running the script, the following files are generated:

* `books.csv`
* `books.xlsx`

Both files contain cleaned and structured book data ready for analysis.

## 🧠 Project Highlights

This project demonstrates:

* Real-world scraping techniques
* Handling multi-level page navigation
* HTML structure analysis
* Data pipeline thinking (ETL)
* Debugging data corruption issues
* Clean, modular Python design



## ⚠️ Notes

* The scraper relies on the current HTML structure of books.toscrape.com
* Some fields use positional HTML logic where no class/id is available
* If the site layout changes, selectors may need adjustment

## ▶️ How to Run

1. Install dependencies:

   * pandas
   * requests
   * beautifulsoup4
   * openpyxl

2. Run the script:

```
python scraper.py
```

3. Check generated CSV and Excel files in the project directory.

