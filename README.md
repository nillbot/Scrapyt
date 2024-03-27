# Scrapyt
 Scrape various search engines with python 

 # Usage

 duckduckgo
 ```python
from Scrapyt.engines.duckduckgo import DuckDuckGoScraper

scraper = DuckDuckGoScraper(browser="Firefox", query="python")
scraper.perform_search(pages=2)
links = scraper.extract_links()
for link in links:
    print(link)
scraper.close()
```
