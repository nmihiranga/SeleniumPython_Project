import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFilteration:

    # initialize webdriver
    def __init__(self, driver:WebDriver):
        self.driver = driver

    # 5 star apply
    def apply_star_rating(self): # * is to get multiple values
        five_star_rating = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-item="class:class=5"]')
        time.sleep(3)
        five_star_rating.click()

    # price low to high apply
    def price_lowest_first(self):
        element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        element.click()
        time.sleep(3)
        low_to_high = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        time.sleep(3)
        low_to_high.click()
