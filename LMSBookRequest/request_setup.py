from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RequestBook:
    def __init__(self,driver):    
        self.driver=driver  

        # LMS book request menuitem
        self.lms_member = (By.XPATH, "//a[@data-menu-xmlid='lms_book_request.lms_book_request_menu']")

        #NEW
        self.new=(By.XPATH, "//button[@class='btn btn-primary o-kanban-button-new']")

        self.name=(By.ID,"name")
        self.genre=(By.ID,"genre")
        self.author=(By.ID,"author")
        self.language=(By.ID,"language")
        self.publisher=(By.ID,"publisher")
        self.mrp=(By.ID,"price")

        #save book
        self.save_icon = (By.CLASS_NAME, "fa-cloud-upload")

    def open_lmsrequest(self):
        try:
            lms_book=self.driver.find_element(*self.lms_member).click()
            time.sleep(2)
        except Exception as exp:
            print("Failed: Request Book Menuitem unable to click")
            print(exp)
        else:
            print("Success: Opened Book Request")

    def click_new(self):
        try:
            new=self.driver.find_element(*self.new).click()
            time.sleep(3)
        except Exception as E:
            print("Failed: Failed to click a new")
            print(E)

    def requested_book_info(self,**kwargs):
        try:
            name = self.driver.find_element(*self.name).send_keys(kwargs.get("name"))
            genre = self.driver.find_element(*self.genre).send_keys(kwargs.get("genre"))
            author = self.driver.find_element(*self.author).send_keys(kwargs.get("author"))
            langage = self.driver.find_element(*self.language).send_keys(kwargs.get("language"))
            publisher = self.driver.find_element(*self.publisher).send_keys(kwargs.get("publisher"))
            mrp_erase = self.driver.find_element(*self.mrp).send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
            mrp = self.driver.find_element(*self.mrp).send_keys(kwargs.get("mrp"))
            time.sleep(3)
        except Exception as E:
            print("Failed: Failed to Fill Request Book Information")
            print(E)
        else:
            print("Success: Filled Request Book Information")

    def save(self):
        try:
            # save the author information
            save_icon = self.driver.find_element(*self.save_icon)
            save_icon.click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
        except Exception as E:
            print("Failed: Failed To request book")
            print(E)
        else:
            print("Success: Book Requested")


        
    
