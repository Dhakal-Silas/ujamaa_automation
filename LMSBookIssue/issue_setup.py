from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LMSBookIssue:
    def __init__(self, driver):
        self.driver = driver

        # LMS Issue a Book menuitem
        self.book_issue = (By.XPATH,"//button[@data-menu-xmlid='lms_book_issue.lms_book_issue_menu']")
        self.issue_a_book = (By.XPATH,"//a[@data-menu-xmlid='lms_book_issue.lms_quick_book_issue_menu']")
 
        # Member Fields
        self.member = (By.ID, "member_id")
        self.book = (By.ID, "book_id")
        self.issued_date = (By.ID, "issued_date")

        #buttons
        self.issue = (By.XPATH,"//button[@name='action_view_new_issue_form']")
        self.reset = (By.XPATH,"//button[@name='reset_form']")
        self.ok = (By.XPATH, "//div[@class='o_dialog_container modal-open']//button[contains(text(), 'Ok')]")
        self.issuetext = (By.XPATH, "//*[text()='Issue a Book ']")

        self.autocomplete_dropdown = (By.CLASS_NAME, "o-autocomplete--dropdown-item")

    def open_LMSBook_Issue(self):
        try:
            book_issue = self.driver.find_element(*self.book_issue).click()
            time.sleep(3)
        except Exception as exp:
            print("Failed: Failed to open Issue a Book")
            print(exp)
        else:
            print("Success: Opened Issue a Book page")

    def ClickIssueaBook(self):
        try:
            self.driver.find_element(*self.issue_a_book).click()
            time.sleep(2)
        except Exception as exp:
            print("Failed: Failed to open issue a book")
            print(exp)
        
    def IssueaBook(self,**kwargs):
        try:
            self.driver.find_element(*self.member).send_keys(kwargs.get("member"))
            time.sleep(2)
            member_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if member_options:
                member_options[0].click()
            time.sleep(2)

            book_element= self.driver.find_element(*self.book)
            if book_element.get_attribute("value").strip() == "":
                book_element.send_keys(kwargs.get("book"))
                time.sleep(2)
                book_options = self.driver.find_elements(*self.autocomplete_dropdown)
                if book_options:
                    book_options[0].click()
            else:
                print("continue")
            time.sleep(2)

            self.driver.find_element(*self.issued_date).clear()
            self.driver.find_element(*self.issued_date).send_keys(kwargs.get("issued_date"))
            self.driver.find_element(*self.issuetext).click()

            time.sleep(3)
        except Exception as exp:
            print("Failed: Failed to fill Book Issue Form")
            print(exp)
        else:
            print("Success: Filled Book Issue Form")

    def ResetButton(self):
        self.driver.find_element(*self.reset).click()
        time.sleep(2)

    def IssueButton(self):
        self.driver.find_element(*self.issue).click()
        try:
            WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='o_dialog_container modal-open']"))
            )

            ok_button = self.driver.find_element(*self.ok)
            ok_button.click()
            print("OK clicked for member")
        except Exception as exp:
            print(exp)
        time.sleep(2)
