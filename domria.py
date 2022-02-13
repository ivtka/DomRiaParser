import time
import constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from prettytable import PrettyTable

from realty import Realty


class DomRia(webdriver.Chrome):
    def __init__(self, driver_path=r"/home/ivtkac/Developments/python/chromedriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(DomRia, self).__init__()

    def __exit__(self, *args) -> None:
        return super().__exit__(*args)

    def load_page(self):
        self.get(const.BASE_URL)

    def select_city(self, city: str) -> None:
        city_element = self.find_element_by_css_selector(
            'input[placeholder="Введіть місто"]')
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

    def report(self):
        realty_boxes = self.find_element(By.ID, 'domSearchPanel')

        realties = Realty(realty_boxes)
        table = PrettyTable(
            field_names=["Realty Location", "Realty Price", "URL"])
        table.add_rows(realties.pull_realties())
        print(table)