# Scrapyt

Scrapyt is a Python library that allows you to scrape various search engines easily. Currently, it supports DuckDuckGo.

## Usage

### DuckDuckGo

```python
from Scrapyt.engines.duckduckgo import DuckDuckGoScraper

# Create an instance of DuckDuckGoScraper, specifying the browser (Firefox) and the search query ("python").
scraper = DuckDuckGoScraper(browser="Firefox", query="python")

# Scrape search results for 2 pages.
scraper.scrape_search_results(pages=2)

# Extract links from the scraped search results.
links = scraper.extract_links()

# Print each extracted link.
for link in links:
    print(link)

# Close the WebDriver session.
scraper.close()
