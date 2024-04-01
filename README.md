# Scrapyt

Scrapyt is a Python library that allows you to scrape various search engines easily. Currently, it supports DuckDuckGo.

## Install

You'll need to install selenium

```
pip install selenium
```

## Usage

### DuckDuckGo

```python
from Scrapyt.engines.duckduckgo import DuckDuckGoScraper

# Create an instance of DuckDuckGoScraper, specifying the browser (Firefox) and the search query ("python").
scraper = DuckDuckGoScraper(browser="Chrome", timeout=20) # Timeout specifies after how much time should the scraper give up if element is not found (recommended: 20)

# Scrape search results for 2 pages.
scraper.perform_search(query="Python", pages=2)

# Extract links from the scraped search results.
links = scraper.extract_links()

# Print each extracted link.
for link in links:
    print(link)

# Close the WebDriver session.
scraper.close()
```
