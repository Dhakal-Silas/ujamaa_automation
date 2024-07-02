from .author_setup import LMSAuthors
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
load_dotenv()

class LMSAuthorTest:
    def __init__(self, driver):
        self.driver = driver
        
    authors_info = {
        "name": os.getenv("LMSAuthor_NAME"),
        "country": os.getenv("LMSAuthor_COUNTRY"),
        "language": os.getenv("LMSAuthor_LANGUAGE"),
    }
    author_books = {
        "search": os.getenv("LMSAuthorBook_SEARCH").split(",")
    }
    new_books = {
        "name": os.getenv("LMSAuthorBook_NAME"),
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

    def author_creation(self):
        lms_author = LMSAuthors(self.driver)
        lms_author.open_lms_author()
        lms_author.click_new()

        author_name = lms_author.new_author(**self.authors_info)
        if author_name:
            self.new_books["authors"].append(author_name)

        # lms_author.new_author(**self.authors_info)
        lms_author.SearchBookFromAuthor(**self.author_books)
        lms_author.NewBookFromAuthor(**self.new_books)
        lms_author.saveandclose()