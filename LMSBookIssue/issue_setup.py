from selenium.webdriver.common.by import By
import time, os

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

        self.autocomplete_dropdown = (By.CLASS_NAME, "o-autocomplete--dropdown-item")

        self.issue_details = {
            "member": os.getenv("LMSMember_NAME"),
            "book": os.getenv("LMSIssue_BOOK"),
            "issued_date": os.getenv("LMSIssue_IssueDate"),
        }

    def open_LMSBook_Issue(self):
        try:
            book_issue = self.driver.find_element(*self.book_issue).click()
            time.sleep(2)
        except Exception as exp:
            print("Failed: Failed to open Issue a Book")
            print(exp)
        else:
            print("Success: Opened Issue a Book page")

    def IssueaBook(self):
        try:
            self.driver.find_element(*self.member).send_keys(self.issue_details.get("member"))
            time.sleep(2)
            member_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if member_options:
                member_options[0].click()

            self.driver.find_element(*self.book).send_keys(self.issue_details.get("book"))
            time.sleep(2)
            book_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if book_options:
                book_options[0].click()
            
            self.driver.find_element(*self.issued_date).clear()
            self.driver.find_element(*self.issued_date).send_keys(self.issue_details.get("issued_date"))
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
        time.sleep(2)

class LMSBookTest:
    def __init__(self, driver):
        self.driver = driver

    def issue_creation(self):
        lms_book_issue=LMSBookIssue(self.driver)
        lms_book_issue.open_LMSBook_Issue()
        lms_book_issue.IssueaBook()
        # lms_book_issue.ResetButton()
        lms_book_issue.IssueButton()
        