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

    def author_creation(self):
        lms_author = LMSAuthors(self.driver)
        lms_author.open_lms_author()
        lms_author.new_author(**self.authors_info)
        lms_author.save_author()