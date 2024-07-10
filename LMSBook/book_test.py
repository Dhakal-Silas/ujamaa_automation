from .newbook import LMSBook
from .issuebook_setup import IssueBook 
from .checkinbook_setup import CheckInBook
from selenium.webdriver.common.by import By
import os,time
from dotenv import load_dotenv
load_dotenv()

class LMSBookTest:
    def __init__(self, driver):
        self.driver = driver
        self.lms_book = LMSBook(driver)  
        self.issuebook = IssueBook(driver)
        self.checkinbook = CheckInBook(driver)
        
    book_details = {
        "name": os.getenv("LMSBook_NAME"),
        "isbn": os.getenv("LMSBook_ISBN"),
        "authors": os.getenv("LMSBook_AUTHORS").split(","),
        "country": os.getenv("LMSBook_COUNTRY"),
        "mrp": os.getenv("LMSBook_MRP"),
        "language": os.getenv("LMSBook_LANGUAGE"),
        "genre": os.getenv("LMSBook_GENRE").split(","),
        "series": os.getenv("LMSBook_SERIES") == 'True',
        "shelf": os.getenv("LMSBook_SHELF"),
        "is_translated": os.getenv("LMSBook_IS_TRANSLATED") == 'True',
        "translated_by": os.getenv("LMSBook_TRANSLATED_BY"),
        "translated_from": os.getenv("LMSBook_TRANSLATED_FROM"),
        "translated_to": os.getenv("LMSBook_TRANSLATED_TO"),
        "publisher": os.getenv("LMSBook_PUBLISHER"),
        "date_published": os.getenv("LMSBook_DATE_PUBLISHED"),
        "edition": os.getenv("LMSBook_EDITION"),
        "pages": int(os.getenv("LMSBook_PAGES")),
        "write_description": os.getenv("LMSBook_DESCRIPTION"),
    }

    search_book = {
        "search_book_name": os.getenv("Book_NAME"),
    }

    member_details = {
        "member": os.getenv("LMSIssue_MEMBER"),
        "issued_date": os.getenv("LMSIssue_IssueDate"),
    }
    
    def book_creation(self):
        self.lms_book.open_lms_book()
        self.lms_book.click_new_book()
        self.lms_book.fill_book_information(**self.book_details)
        self.lms_book.fill_book_information_publisher(**self.book_details)
        self.lms_book.book_fill_information_description(**self.book_details)
        self.lms_book.save_author()

    def issue_from_book(self):
        self.lms_book.open_lms_book()
        self.issuebook.search_book(**self.search_book)
        self.issuebook.click_issue()
        self.issuebook.IssueBook(**self.member_details)
        self.issuebook.save()

    def checkin_from_book(self):
        self.lms_book.open_lms_book()
        self.checkinbook.search_book_checkin(**self.search_book)
        self.checkinbook.click_checkin()