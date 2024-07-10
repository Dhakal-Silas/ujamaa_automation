from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LMSGenre:
    def __init__(self,driver):    
        self.driver=driver  

        # LMS member menuitem
        self.lms_genre = (By.XPATH, "//a[@data-menu-xmlid='lms_book.lms_book_genre_menu']")

        #NEW
        self.new=(By.XPATH, "//button[@class='btn btn-primary o-kanban-button-new']")

        #Genre Fields
        self.name=(By.ID,"name")
        self.color_buttom=(By.XPATH,"//button[@title='No color']")

        # Save Information
        self.save_icon = (By.CLASS_NAME, "fa-cloud-upload")

    def open_lms_genre(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.lms_genre)
            ).click()
        except Exception as exp:
            print("Failed: Genre Menuitem unable to click")
            print(exp)
        else:
            print("Success: Open LMS Genre")
    
    def new_genre(self,**kwargs):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.new)
            )
            new=self.driver.find_element(*self.new).click()

            name = self.driver.find_element(*self.name).send_keys(kwargs.get("name"))
            click_color_button = self.driver.find_element(*self.color_buttom).click()
            time.sleep(2)
            color_button_xpath = f"//button[@title='{kwargs.get('choice')}']"
            color=self.driver.find_element(By.XPATH,color_button_xpath).click()
            time.sleep(3)
        except Exception as E:
            print("Failed: Failed to fill form of a new genre")
            print(E)
        else:
            print("Success: Form filled of a new genre")

    def save_genre(self):
        try:
            # save the member information
            save_icon = self.driver.find_element(*self.save_icon)
            save_icon.click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
        except Exception as E:
            print("Failed: Failed To Save Genre Information")
            print(E)
        else:
            print("Success: Saved Genre Information")
