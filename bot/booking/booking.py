import time
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filteration import BookingFilteration

class Booking(webdriver.Chrome):

    # initialize webdriver
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    # browser close
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # popup close
    def popup_close(self):
        try:
            close_btn = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign in information."]')
            close_btn.click()
        except:
            print('skipping...')

    # home page navigate
    def land_first_page(self):
        self.get(const.BASE_URL)

    # selecting a place to book
    def select_place_to_go(self, placeToGo):
        search = self.find_element(By.ID, ':re:')
        search.clear()
        search.send_keys(placeToGo)
        time.sleep(3)
        first_result = self.find_element(By.ID, 'autocomplete-result-0')
        first_result.click()

    # selecting check in and check out dates
    def select_date(self, checkInDate, checkOutDate):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td > span[data-date="{checkInDate}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'td > span[data-date="{checkOutDate}"]')
        check_out_element.click()

    # selecting people
    def select_people(self, adults=1, rooms=1):
        selection_element = self.find_element(By.XPATH, '//*[@id="indexsearch"]/div[2]/div/form/div[1]/div[3]/div')
        selection_element.click()

        # selecting adults
        while True:
            decrease_adults_element = self.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[1]/div[2]/button[1]')
            decrease_adults_element.click()
            adults_value_element = self.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute('value')

            if int(adults_value) == 1:
                break

        increase_adults_element = self.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[1]/div[2]/button[2]')
        for _ in range(adults - 1):
            increase_adults_element.click()

        # selecting children
        increase_children_element = self.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[2]/div[2]/button[2]')
        increase_children_element.click()
        age_select_button = self.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[3]/div/div')
        age_select_button.click()
        time.sleep(1)
        age_select = self.find_element(By.CSS_SELECTOR, 'option[value="2"]')
        age_select.click()

        # selecting room
        increase_rooms_element = self.find_element(By.XPATH, '//*[@id=":rf:"]/div/div[5]/div[2]/button[2]')
        for _ in range(rooms - 1):
            increase_rooms_element.click()

        done_button = self.find_element(By.XPATH, '//*[@id=":rf:"]/button')
        done_button.click()

    # click search button
    def click_search(self):
        search_btn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_btn.click()
        time.sleep(5)
        self.popup_close()

    # filterations
    def apply_filterations(self):
        filteration = BookingFilteration(driver=self)
        filteration.apply_star_rating()
        filteration.price_lowest_first()