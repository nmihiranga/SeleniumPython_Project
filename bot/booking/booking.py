import time
from concurrent.futures import thread

import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options



class Booking(webdriver.Chrome):

    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):  #browser close
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)


    '''def change_currency(self, currency=None):
        currency_element = self.find_element(By.XPATH, '//*[@id="b2indexPage"]/div[2]/div/div/header/nav[1]/div[2]/span[1]/button')
        currency_element.click()
        change_element = self.find_element(By.XPATH, '//*[@id="b2indexPage"]/div[21]/div/div/div/div/div[2]/div/div[2]/div/div/ul[1]/li[1]/button/div/div[1]/span/div')
        change_element.click()
    '''

    def select_place_to_go(self, placeToGo):
        search = self.find_element(By.ID, ':re:')
        search.clear()
        search.send_keys(placeToGo)
        time.sleep(5)
        first_result = self.find_element(By.ID, 'autocomplete-result-0')
        first_result.click()

    def select_date(self, checkInDate, checkOutDate):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td > span[data-date="{checkInDate}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'td > span[data-date="{checkOutDate}"]')
        check_out_element.click()

    def select_people(self):
        selection_element = self.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[3]/div')
        selection_element.click()
        while(True):
            pass