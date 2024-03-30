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
