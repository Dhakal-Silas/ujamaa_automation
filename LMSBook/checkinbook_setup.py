from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckInBook:
    def __init__(self,driver):    
        self.driver=driver  

        # LMS book menuitem
        self.lms_member = (By.XPATH, "//a[@data-menu-xmlid='lms_book.lms_book_menu']")
        
        self.searchbook = (By.XPATH, "//input[@role='searchbox']")
        self.findbook = (By.XPATH, "//button[@name='action_check_in_book' and .//span[text()='CHECK-IN']]")

    def search_book_checkin(self, **kwargs):
        try:
            search_book = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.searchbook))
            search_book.send_keys(kwargs.get("search_book_name"))
            search_book.send_keys(Keys.ENTER)
            print("Success: Searched book")
            time.sleep(4)
        except Exception as exp:
            print("Failed: Failed to search by book name")
            print(exp)

    def click_checkin(self):
        try:
            checkin_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.findbook))
            checkin_button.click()
            print("Success: Success to check in")
            time.sleep(5)
        except Exception as exp:
            print("Failed: Failed to check in")
            print(exp)