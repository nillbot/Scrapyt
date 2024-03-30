import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Scrapyt.logger import _setup_logger
from Scrapyt.exceptions import MaxResultsReachedException

class DuckDuckGoScraper:
    def __init__(self, browser="Firefox", query="site:github.com inurl:/nillbot", timeout=10):
        self.query = query
        self.timeout = timeout
        self.logger = _setup_logger()
        self.driver = self._initialize_driver(browser)

    def _initialize_driver(self, browser):
        try:
            if browser.lower() == "chrome":
                return webdriver.Chrome()
            elif browser.lower() == "firefox":
                return webdriver.Firefox()
            else:
                raise ValueError("Unsupported browser. Please specify 'chrome' or 'firefox'.")
        except Exception as e:
            self.logger.error(f"Error initializing WebDriver: {e}")
            exit()

    def perform_search(self, pages):
            self._search()
            if pages == 1:
                self._scroll()
            else:
                for _ in range(pages-1):
                    self._scroll()
                    try:
                        self._load_more_results()
                    except MaxResultsReachedException:
                        self.logger.error("Unable to load more search results, consider increasing timeout if you believe this is wrong")
                        break
                        self._wait_until_more_results_loaded()
    
    def _search(self):
        try:
            url = f"https://duckduckgo.com/?q={self.query}"
            self.driver.get(url)
        except Exception as e:
            self.logger.error(f"Error navigating to search page: {e}")
            exit()

    def _scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _load_more_results(self):
        try:
            button = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, "//button[@id='more-results']")))
            button.click()
        except TimeoutException:
            self.logger.warning("Timed out waiting for 'Load More Results' button. Most probably end of results reached or you set the timeout too low")
            raise MaxResultsReachedException()
    
    def _wait_until_more_results_loaded(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, "//button[not(@disabled='')]")))
        except TimeoutException:
            self.logger.error("Timed out waiting for more results to load. This usually happens when 'more results' button wasn't clicked or you set the timeout too low")
            exit()
            
    def extract_links(self):
        time.sleep(1)
        try:
            self._scroll()
            link_elements = self.driver.find_elements(By.XPATH, "//a[@data-testid='result-extras-url-link']")
            extracted_links = [link_element.get_attribute("href") for link_element in link_elements]
            return extracted_links
        except Exception as e:
            self.logger.error(f"Error extracting links: {e}")
            exit()

    def close(self):
        try:
            self.driver.quit()
        except Exception as e:
            self.logger.error(f"Error closing WebDriver: {e}")
            raise
