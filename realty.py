from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

import config


class Realty:
    def __init__(self, boxes_section_element: WebElement):
        self.boxes_section_element = boxes_section_element
        self.realty_boxes = self.pull_realty_boxes()

    def pull_realty_boxes(self):
        return self.boxes_section_element.find_elements(By.CLASS_NAME,
                                                        'realty-item')

    def pull_realties(self):
        collection = []
        for realty_boxe in self.realty_boxes:
            realty = realty_boxe.find_element(
                By.CLASS_NAME, 'realty-link')
            realty_location = realty.get_attribute('title')
            print(realty_location)
            realty_price = realty_boxe.find_element(By.CSS_SELECTOR,
                                                    'b.size18'
                                                    ).get_attribute(
                'innerHTML').strip()
            realty_link = realty.get_attribute('href')

            collection.append([realty_location, realty_price, realty_link])

        return collection
