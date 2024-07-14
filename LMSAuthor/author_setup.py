from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from LMSBook.newbook import LMSBook
class LMSAuthors():
    def __init__(self,driver):    
        self.driver=driver 
        # LMS author menuitem
        self.lms_author = (By.XPATH, "//a[@data-menu-xmlid='lms_book.lms_book_author_menu']")

        #NEW
        self.new=(By.XPATH, "//button[@class='btn btn-primary o-kanban-button-new']")

        #Author Fields
        self.name=(By.XPATH, "//div[@name='name']/input[@id='name']")
        self.select_country=(By.XPATH,"//h4[span[text()='Country: ']]//div[contains(@class, 'o_field_widget') and contains(@class, 'o_required_modifier') and contains(@class, 'o_field_many2one')]//input[@id='country_id']")
        self.select_language=(By.XPATH,"//h4[span[text()='Language: ']]//div[contains(@class, 'o_field_widget') and contains(@class, 'o_required_modifier') and contains(@class, 'o_field_many2one')]//input[@id='language_id']")
        
        self.autocomplete_dropdown = (By.CLASS_NAME, "o-autocomplete--dropdown-item")

        #Add author by search
        self.add=(By.XPATH, "//button[@title='Create record']")
        self.searchbox=(By.XPATH, "//input[@role='searchbox']")
        self.book=(By.XPATH, "//tr[@class='o_data_row']")

        #Add author by new
        self.newbook=(By.XPATH, "//button[@class='btn btn-primary o_create_button' and @data-hotkey='c']")
        self.save_close = (By.XPATH, "//button[contains(@class, 'o_form_button_save') and contains(text(), 'Save & Close')]")

        # Save Information
        self.save_icon = (By.CLASS_NAME, "fa-cloud-upload")

    def open_lms_author(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.lms_author)).click()
        except Exception as exp:
            print("Failed: Author Menuitem unable to click")
            print(exp)
        else:
            print("Success: Opened LMS Author")

    def click_new(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.new))
            new=self.driver.find_element(*self.new).click()
        except Exception as E:
            print("Failed: Failed to click new button on author")
            print(E)

    def new_author(self,**kwargs):
        try:
            name = self.driver.find_element(*self.name).send_keys(kwargs.get("name"))

            #country
            country_input = self.driver.find_element(*self.select_country).send_keys(kwargs.get("country"))
            time.sleep(2)
            country_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if country_options:
                country_options[0].click()

            #language
            language_input = self.driver.find_element(*self.select_language).send_keys(kwargs.get("language"))
            time.sleep(2)
            language_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if language_options:
                language_options[0].click()
            time.sleep(2)

            try:
                # save the author information
                save_icon = self.driver.find_element(*self.save_icon)
                save_icon.click()
                self.driver.implicitly_wait(2)
            except Exception as E:
                print("Failed: Failed To Save Author Information")
                print(E)
            else:
                print("Success: Saved Author Information")
                return kwargs.get("name")

        except Exception as E:
            print("Failed: Failed to create a new author")
            print(E)

    def SearchBookFromAuthor(self,**kwargs):
        try:
            books=kwargs.get("search",[])
            for book in books:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.add))
                add=self.driver.find_element(*self.add).click()
                time.sleep(2)

                #search book
                search=self.driver.find_element(*self.searchbox)
                search.click()
                time.sleep(2)
                search_book=search.send_keys(book)
                search_enter=search.send_keys(Keys.RETURN)
                time.sleep(2)

                #click book
                author_books = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.book))
                if author_books:
                    author_books[0].click()
                time.sleep(2)
            print("Success: Searched Book Added to Author")
        except Exception as E:
            print("Failed: Failed to create a new author")
            print(E)
    
    def NewBookFromAuthor(self,**new_book_details):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add)).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.newbook)).click()

            lms_book = LMSBook(self.driver)
            lms_book.fill_book_information(**new_book_details)
            time.sleep(2)
            lms_book.fill_book_information_publisher(**new_book_details)
            time.sleep(2)
            lms_book.book_fill_information_description(**new_book_details)
            time.sleep(2)
            print("Success: New Book Added to Author")
        except Exception as E:
            print("Failed: Failed to create a new author")
            print(E)   

    def saveandclose(self):
        try:    
            save_and_close = self.driver.find_element(*self.save_close)
            save_and_close.click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
        except Exception as E:
            print("Failed: Failed to save and close")
            print(E)
        else:
            print("Success: Saved and Closed")

    def save(self):
        try:
            # save the member information
            save_icon = self.driver.find_element(*self.save_icon)
            save_icon.click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
        except Exception as E:
            print("Failed: Failed To Save Member Information")
            print(E)
        else:
            print("Success: Saved Author With all added books")