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

# Create an instance of DuckDuckGoScraper, specifying the browser (Chrome) and the search query ("python").
scraper = DuckDuckGoScraper(browser="Chrome", query="python")

# Scrape search results for 2 pages.
scraper.perform_search(pages=2)

# Extract links from the scraped search results.
links = scraper.extract_links()

# Print each extracted link.
for link in links:
    print(link)

# Close the WebDriver session.
scraper.close()
```

* Original Pages present is less than pages i want to scrape

```python
from Scrapyt.engines.duckduckgo import DuckDuckGoScraper
from Scrapyt.exceptions import MaxResultsReachedException

scraper = DuckDuckGoScraper(browser="Chrome", query="python")

try:
    scraper.perform_search(pages=2)
except MaxResultsReachedException:
    pass

links = scraper.extract_links()
for link in links:
    print(link)

scraper.close()
```
