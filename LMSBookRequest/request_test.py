from .request_setup import RequestBook
from selenium.webdriver.common.by import By
import os

class LMSBookRequestTest:
    def __init__(self, driver):
        self.driver = driver
        self.request = RequestBook(driver)  

    request_book = {
        "name": os.getenv("LMSBookRequest_NAME"),
        "genre": os.getenv("LMSBookRequest__GENRE"),
        "author": os.getenv("LMSBookRequest__AUTHOR"),
        "language": os.getenv("LMSBookRequest__LANGUAGE"),
        "publisher": os.getenv("LMSBookRequest__PUBLISHER"),
        "mrp": os.getenv("LMSBookRequest__MRP"),
    }

    def book_request(self):
        self.request.open_lmsrequest()
        self.request.click_new()
        self.request.requested_book_info(**self.request_book)
        self.request.save()
