import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class DuckDuckGoScraper:
    def __init__(self, browser="Firefox", query="site:github.com inurl:/nillbot", timeout=10):
        self.query = query
        self.timeout = timeout
        self.driver = self._initialize_driver(browser)
        self.logger = self._setup_logger()

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
            raise

    def _setup_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    def _wait_until_more_results_loaded(self):
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, "//button[not(@disabled='')]")))
        except TimeoutException:
            self.logger.warning("Timed out waiting for more results to load")

    def _scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _load_more_results(self):
        try:
            button = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, "//button[@id='more-results']")))
            button.click()
        except TimeoutException:
            self.logger.warning("Timed out waiting for 'Load More' button")
        except NoSuchElementException:
            self.logger.warning("'Load More' button not found")

    def perform_search(self, pages):
        try:
            self._search()
            if pages == 1:
                self._scroll()
            else:
                for _ in range(pages-1):
                    self._scroll()
                    self._load_more_results()
                    self._wait_until_more_results_loaded()
                self._scroll()
        except Exception as e:
            self.logger.error(f"Error performing search: {e}")
            raise

    def _search(self):
        try:
            url = f"https://duckduckgo.com/?q={self.query}"
            self.driver.get(url)
        except Exception as e:
            self.logger.error(f"Error navigating to search page: {e}")
            raise

    def extract_links(self):
        try:
            link_elements = self.driver.find_elements(By.XPATH, "//a[@data-testid='result-extras-url-link']")
            extracted_links = [link_element.get_attribute("href") for link_element in link_elements]
            return extracted_links
        except Exception as e:
            self.logger.error(f"Error extracting links: {e}")
            raise

    def close(self):
        try:
            self.driver.quit()
        except Exception as e:
            self.logger.error(f"Error closing WebDriver: {e}")
            raise
