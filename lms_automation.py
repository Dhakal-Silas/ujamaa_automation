from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time

from dotenv import load_dotenv
load_dotenv()

from LMSMember.member_test import LMSMemberTest
from LMSAuthor.author_test import LMSAuthorTest
from LMSBook.book_test import LMSBookTest
from LMSGenre.genre_test import LMSGenreTest
from LMSBookIssue.test import LMSBookIssueTest
from LMSBookRequest.request_test import LMSBookRequestTest

class LMS:
    def __init__(self):
        self.service = webdriver.ChromeService()
        self.driver = webdriver.Chrome(service = self.service)
        self.url="http://localhost:8069/web/login"
        try:
            self.driver.get(self.url)
            self.driver.maximize_window() 
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "login"))
            )
        except Exception  as exp:
            print("Failed: Localhost not running or server Error")
            print(exp)
            exit(1)

        #login(email,password)
        self.email = (By.ID, "login")
        self.password = (By.ID, "password")
        self.login_button = (By.XPATH, "//button[normalize-space()='Log in']")

        #LMS  rootmenu
        self.apps = (By.XPATH, "//button[@title='Home Menu']")
        self.LMS = (By.XPATH, "//a[@data-menu-xmlid='va_lms.lms_root_menu']")

    def login(self,uniquemail,pwd):
        try:
            email_element=self.driver.find_element(*self.email)
            email_element.send_keys(uniquemail);
            password_element=self.driver.find_element(*self.password)
            password_element.send_keys(pwd)
            login_button = self.driver.find_element(*self.login_button)
            login_button.click()

            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.apps)
            )
        except Exception as exp:
            print("Failed: Server Login")
            print(exp)
        else:
            print("Login Success")
    
    def open_lms(self):
        try:
            apps=self.driver.find_element(*self.apps).click()
            lms=self.driver.find_element(*self.LMS).click()
            time.sleep(5)
        except Exception as exp:
            print("Failed: Unable to click LMS")
            print(exp)
        else:
            print("Success: Opened LMS Root Menu")

if __name__ == "__main__":
    lms=LMS()

    #login into portal
    lms.login(os.getenv("EMAIL"),os.getenv("PASSWORD"))
    lms.open_lms()

    # Add Member
    lms_member_test=LMSMemberTest(lms.driver)
    lms_member_test.member_creation()

    #Add Genre
    lms_genre_test=LMSGenreTest(lms.driver)
    lms_genre_test.genre_creation()

    # #Add Author with the author's books
    lms_author_test=LMSAuthorTest(lms.driver)
    lms_author_test.author_creation()

    #Add Book and issue book from Book menuitem
    lms_book_test=LMSBookTest(lms.driver)
    lms_book_test.book_creation()
    lms_book_test.issue_from_book()
    lms_book_test.checkin_from_book()

    #Issue a Book and return issued book from Book Issue menuitem
    lms_book_issue_test=LMSBookIssueTest(lms.driver)
    lms_book_issue_test.issue_book_creation()
    lms_book_issue_test.book_return_issue_history()

    # Request a Book
    lms_request_book=LMSBookRequestTest(lms.driver)
    lms_request_book.book_request()