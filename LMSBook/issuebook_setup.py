from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from LMSBookIssue.issue_setup import LMSBookIssue
import time

class IssueBook:
    def __init__(self,driver):    
        self.driver=driver  

        # LMS book menuitem
        self.lms_member = (By.XPATH, "//a[@data-menu-xmlid='lms_book.lms_book_menu']")
        
        self.searchbook = (By.XPATH, "//input[@role='searchbox']")
        self.selectbook = (By.XPATH, "//button[@name='action_book_issue_view' and .//span[text()='Issue']]")

        self.savee = (By.XPATH, "//button[@data-hotkey='s']")

    def search_book(self, **kwargs):
        try:
            search_book = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.searchbook))
            search_book.send_keys(kwargs.get("search_book_name"))
            search_book.send_keys(Keys.ENTER)
            print("Success: Searched book")
            time.sleep(4)
        except Exception as exp:
            print("Failed: Failed to search by book name")
            print(exp)

    def click_issue(self):
        try:
            book = self.driver.find_element(*self.selectbook)
            book.click()
            time.sleep(2)
        except Exception as exp:
            print("Failed: Failed to search by book name")
            print(exp)

    def IssueBook(self,**member_details):
        try:
            issue_details=LMSBookIssue(self.driver)
            issue_details.IssueaBook(**member_details)
            time.sleep(2)
        except Exception as exp:
            print("Failed: Failed to fill book issuer details from book")
            print(exp)

    def save(self):
        try:
            save = self.driver.find_element(*self.savee)
            save.click()
        except Exception as exp:
            print("Failed: Failed to Save")
            print(exp)
