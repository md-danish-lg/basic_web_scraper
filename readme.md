
# 📚 Basic Web Scraper

A Python-based web scraper that extracts book data from **books.toscrape.com** and saves it into CSV and Excel files.

This project is built as a multi-day learning project focused on writing **more flexible, production-style scrapers**.

---

## 🚀 Features

* Scrapes book data from books.toscrape.com
* Supports **CLI arguments** for flexible usage
* Extracts:

  * Book name
  * Price
  * Availability
  * Product link
  * Product description (from product page)
* Saves data to:

  * CSV file
  * Excel file
* Handles missing data safely
* More robust scraping logic

---

## 🛠 Technologies Used

* Python 3
* Requests
* BeautifulSoup (bs4)
* Pandas

---

## ▶ How to Run (CLI Arguments)

This script requires **command-line arguments**.

Example usage:

```bash
python scraper.py <start-page> <end-page> <output_file_name>>
```


This allows you to control scraping behavior **without changing the code**.

---

## 📂 Output Files

Based on CLI input, the script generates:

* `<output>.csv`
* `<output>.xlsx`

Example:

```
books.csv
books.xlsx
```

---

## 📌 Project Goals

This project focuses on:

* Building configurable scrapers using CLI
* Cleaner data pipelines
* Better structure for scaling scrapers
* Real-world scraping practices
* Git + GitHub workflow

---

## 🧪 Current Status (Day 5)

* CLI argument support added ✅
* Product page scraping added ✅
* Data extraction improvements ✅
* CSV/Excel consistency fixes ✅
* Ongoing validation improvements

---

## ⚠ Disclaimer

This scraper is for **educational purposes only**.
Always respect websites’ terms of service.

