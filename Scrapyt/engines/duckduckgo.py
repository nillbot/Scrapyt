from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DuckDuckGoScraper:
    
    def __init__(self, browser="Firefox", query="site:github.com inurl:/nillbot"):
        self.query = query
        if browser == "Chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

    def scrape(self, pages):
        self.search()
        if pages == 1:
            self.scroll
        else:
            for _ in range(pages-1):
                self.scroll()
                self.load_more_results()
                self.wait_until_page_loaded()

            self.scroll()

    def search(self):
        url = f"https://duckduckgo.com/?q={self.query}"
        self.driver.get(url)

    def extract_links(self):
        link_elements = self.driver.find_elements(By.XPATH, "//a[@data-testid='result-extras-url-link']")
        extracted_links = [link_element.get_attribute("href") for link_element in link_elements]
        return extracted_links
    
    def wait_until_page_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[not(@disabled='')]")))
    
    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def load_more_results(self):
        try:
            button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='more-results']")))
            button.click()
        except Exception as e:
            print(f"Error while loading more results: {e}")

    def close(self):
        self.driver.quit()