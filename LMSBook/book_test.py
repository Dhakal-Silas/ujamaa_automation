from .book_setup import LMSBook
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()

class LMSBookTest:
    def __init__(self, driver):
        self.driver = driver
        
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

    def book_creation(self):
        lms_book = LMSBook(self.driver)
        lms_book.open_lms_book()
        lms_book.click_new_book()
        lms_book.fill_book_information(**self.book_details)
        lms_book.fill_book_information_publisher(**self.book_details)
        lms_book.book_fill_information_description(**self.book_details)
        lms_book.save_author()