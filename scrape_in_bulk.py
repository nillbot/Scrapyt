from Scrapyt.engines.duckduckgo import DuckDuckGoScraper

scraper = DuckDuckGoScraper(browser="Firefox", timeout=20)

# dorks or my query  file
with open("dorks.txt", "r") as f:
    dork_list = f.read().split("\n")

counter = 0
for dork in dork_list:
    counter += 1
    try:
        scraper.perform_search(pages=100, query=f"site:* inurl:/{dork}")
        links = scraper.extract_links()
        for link in links:
            with open("sites.txt", "a") as f:
                f.write(f"{link}\n")
        dork_list.remove(dork)

    except KeyboardInterrupt:
        for dork in dork_list:
            with open(".cache/session.txt", "a") as f:
                f.write(dork + "\n")
        exit()
    
    except:
        pass

    # close and open the browser to bypass potential captcha
    if counter % 10 == 0:
        scraper.close()
        scraper._initialize_driver("Firefox")
