from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

class LMSAuthors:
    def __init__(self,driver):    
        self.driver=driver 

        # LMS author menuitem
        self.lms_author = (By.XPATH, "//a[@data-menu-xmlid='lms_book.lms_book_author_menu']")

        #NEW
        self.new=(By.XPATH, "//button[@class='btn btn-primary o-kanban-button-new']")

        #Author Fields
        self.name=(By.ID,"name")
        self.select_country=(By.ID,"country_id")
        self.select_language=(By.ID,"language_id")
        self.autocomplete_dropdown = (By.CLASS_NAME, "o-autocomplete--dropdown-item")

        # Save Information
        self.save_icon = (By.CLASS_NAME, "fa-cloud-upload")

    def open_lms_author(self):
        try:
            lms_author=self.driver.find_element(*self.lms_author).click()
            time.sleep(2)
        except Exception as exp:
            print("Failed: Author Menuitem unable to click")
            print(exp)
        else:
            print("Success: Opened LMS Author")

    def new_author(self,**kwargs):
        try:
            new=self.driver.find_element(*self.new).click()

            name = self.driver.find_element(*self.name).send_keys(kwargs.get("name"))

            #country
            country_input = self.driver.find_element(*self.select_country).send_keys(kwargs.get("country"))
            time.sleep(2)
            country_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if country_options:
                country_options[0].click()

            #language
            language_input = self.driver.find_element(*self.select_language).send_keys(kwargs.get("language"))
            time.sleep(2)
            language_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if language_options:
                language_options[0].click()

            time.sleep(7)
        except Exception as E:
            print("Failed: Failed to create a new author")
            print(E)
        else:
            print("Success: Created a new author")

    def save_author(self):
        try:
            # save the author information
            save_icon = self.driver.find_element(*self.save_icon)
            save_icon.click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
        except Exception as E:
            print("Failed: Failed To Save Author Information")
            print(E)
        else:
            print("Success: Saved Author Information")