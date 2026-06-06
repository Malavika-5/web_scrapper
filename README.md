# web_scrapper

## Objective

This project scrapes top news headlines from the Indian Express website and saves them to a text file.

## Tools Used

- Python
- Requests
- BeautifulSoup4

## Features

- Fetches webpage content using Requests
- Parses HTML using BeautifulSoup
- Extracts news headlines from multiple HTML tags and classes
- Saves headlines to a text file automatically

## Project Structure

```
Task-3-News-Scraper/
│
├── scrapper.py
├── headlines.txt
└── README.md
```

## Installation

Install the required packages:

```bash
pip install requests beautifulsoup4 lxml
```

## How to Run

Run the Python script:

```bash
python scrapper.py
```

After execution, a file named `headlines.txt` will be created containing the scraped headlines.
