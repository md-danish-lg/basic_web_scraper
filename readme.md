
# 📚 Books to Scrape (CLI Web Scraper)

A Python-based command-line web scraper that extracts book data from **[http://books.toscrape.com/](http://books.toscrape.com/)** and saves the results into CSV and Excel files.

This project was developed progressively over multiple days to practice writing more structured, production-style scraping scripts.

---

## 🚀 Features

* Scrapes multiple catalogue pages
* Visits each product page for detailed data
* Extracts:

  * UPC Code
  * Book Name
  * Price
  * Rating (out of five)
  * Availability
  * Product Description
  * Product Link
* CLI-based configuration
* Logging system (`app.log`)
* CSV and Excel export
* Basic request failure handling
* Throttling using timed delays

---

## 🛠 Technologies Used

* Python 3
* `requests`
* `beautifulsoup4`
* `pandas`
* `logging` (standard library)

---

## ▶ How to Run

This script requires **command-line arguments**.

### Syntax:

```
python scraper.py <start_page> <end_page> [output_name]
```

### Example:

```
python scraper.py 1 3 books_data
```

This will:

* Scrape pages 1 through 3
* Save:

  * `books_data.csv`
  * `books_data.xlsx`
* Generate logs in:

  * `app.log`

If no output name is provided, the default is:

```
output.csv
output.xlsx
```

---

## 📂 Output

The scraper generates:

* `<output>.csv`
* `<output>.xlsx`
* `app.log` (log file)

The price column is cleaned and converted to float before saving.

---

## 🧠 What This Project Demonstrates

* Multi-page web scraping
* Deep page scraping (following product links)
* Structured data extraction
* Command-line interface usage
* Logging and error reporting
* Basic resilience to failed requests
* Clean script entry point using `if __name__ == "__main__"`

---

## ⚠ Known Limitations

* Uses basic error handling (generic exception blocks)
* Assumes consistent page structure
* Does not implement retry logic for failed requests
* Does not validate extracted fields before processing
* No database integration (file-based storage only)
* Uses a simple fixed delay instead of adaptive rate limiting

---

## 🔧 Possible Improvements

Future enhancements could include:

* Replace generic `except` blocks with detailed exception handling
* Add retry mechanism for failed HTTP requests
* Validate extracted data fields before processing
* Improve logging with exception trace details
* Store data in SQLite or another database
* Convert into a class-based scraper architecture
* Add argument parsing using `argparse`
* Implement asynchronous scraping for performance
* Add unit tests for extraction logic

---

## 📌 Disclaimer

This project is for **educational purposes only**.
Always respect a website’s terms of service and robots.txt when scraping.

