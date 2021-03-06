import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from realty import Realty

import config


class UserData:
    def __init__(self, name):
        self.name = name
        self.city = None
        self.state = None
        self.start_price = None
        self.end_price = None


class DomRia(webdriver.Chrome):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--lang=uk')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--remote-debugging-port=9222')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--window-size=1920x1080')
        self.options.headless = True
        super(DomRia, self).__init__(ChromeDriverManager().install(), chrome_options=self.options)

    def __exit__(self, *args) -> None:
        return super().__exit__(*args)

    def load_page(self):
        self.get(config.DOMRIA_URL)

    def select_city(self, city: str) -> None:
        city_element = self.find_element_by_css_selector(
            'input[placeholder="Введіть місто"]')
        print(city_element.get_attribute("value"))
        city_element.click()
        city_element.send_keys(city)
        city_element.send_keys(Keys.RETURN)
        time.sleep(3)

    def select_state(self, state: str) -> None:
        search_field = self.find_element_by_css_selector(
            'input#autocomplete-1')
        search_field.click()
        selected_state_element = self.find_element_by_xpath(
             f'//label[text()="{state}"]')
        selected_state_element.click()
        time.sleep(3)

    def select_price(self, start_price: int, end_price: int) -> None:
        price_field = self.find_element_by_css_selector(
            'div#mainAdditionalParams_0')
        price_field.click()

        start_price_field = self.find_element_by_css_selector(
            'input[placeholder="Від"]')
        start_price_field.send_keys(start_price)

        end_price_field = self.find_element_by_css_selector(
            'input[placeholder="До"]')
        end_price_field.send_keys(end_price)
        end_price_field.send_keys(Keys.RETURN)
        time.sleep(3)

    def report(self, user_data: UserData) -> list:
        self.load_page()
        self.select_city(user_data.city)
        self.select_state(user_data.state)
        self.select_price(start_price=int(user_data.start_price),
                          end_price=int(user_data.end_price))
        self.refresh()

        realty_boxes = self.find_element(By.ID, 'domSearchPanel')

        realties = Realty(realty_boxes)
        return realties.pull_realties()
