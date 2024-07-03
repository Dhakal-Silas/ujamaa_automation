from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os
from dotenv import load_dotenv
load_dotenv()

class LMSBookReturn:
    def __init__(self,driver):
        self.driver=driver  
        
        # LMS Issue a Book menuitem
        self.book_issue = (By.XPATH,"//button[@data-menu-xmlid='lms_book_issue.lms_book_issue_menu']")
        self.issue_history = (By.XPATH,"//a[@data-menu-xmlid='lms_book_issue.lms_book_issue_history_menu']")

        #search book
        self.searchbook = (By.XPATH, "//input[@role='searchbox']")

        #findbook
        self.state = (By.XPATH, "//span[contains(@class, 'badge rounded-pill') and (text()='Overdue' or text()='Issued')]")

        #checkin
        self.checkin = (By.XPATH, "//button[@name='action_check_in_book']")
    
        
    def open_LMSBook_Issue(self):
        try:
            book_issue = self.driver.find_element(*self.book_issue).click()
            time.sleep(3)
        except Exception as exp:
            print("Failed: Failed to open Issue a Book")
            print(exp)
        else:
            print("Success: Opened Issue a Book page")

    def open_issue_history(self):
        try:
            self.driver.find_element(*self.issue_history).click()
            time.sleep(2)
        except Exception as exp:
            print("Failed: Failed to click Issue History")
            print(exp)
        else:
            print("Success: Clicked Issue History")

    def search_book(self,**kwargs):
        try:
            search_book=self.driver.find_element(*self.searchbook)
            search_book.send_keys(kwargs.get("book"))
            search_book.send_keys(Keys.ENTER)
            time.sleep(4)
        except Exception as exp:
            print("Failed: Failed to search by book name")
            print(exp)

    def find_return_book(self):
        try:
            overdue_issued=self.driver.find_element(*self.state)
            overdue_issued.click()

            WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='o_form_sheet position-relative clearfix']"))
            )

            self.driver.find_element(*self.checkin).click()
            self.driver.find_element(*self.book_issue).click()
            time.sleep(2)
            self.driver.find_element(*self.issue_history).click()
            time.sleep(10)
            print("Success: Book checked in")

        except Exception as exp:
            print("Failed: No book found with state 'issued' or 'overdue'")
            print(exp)

