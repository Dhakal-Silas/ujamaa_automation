from selenium.webdriver.common.by import By
import time

class LMSBook:
    def __init__(self,driver):    
        self.driver=driver  

        # LMS book menuitem
        self.lms_member = (By.XPATH, "//a[@data-menu-xmlid='lms_book.lms_book_menu']")

        #NEW
        self.new=(By.XPATH, "//button[@class='btn btn-primary o-kanban-button-new']")

        # #Book Fields
        self.name = (By.XPATH, "//input[@class='o_input' and @id='name' and @placeholder='Title']")
        
        #book information
        self.isbn=(By.ID,"isbn")
        self.author_ids=(By.ID,"author_ids")
        self.country_id=(By.XPATH,"//div[@class='o_cell o_wrap_input flex-grow-1 flex-sm-grow-0 text-break']//input[@id='country_id']")
        self.MRPprice=(By.ID,"price")

        #book categorization
        self.language_id=(By.XPATH,"//div[@class='o_cell o_wrap_input flex-grow-1 flex-sm-grow-0 text-break']//input[@id='language_id']")
        self.genre_ids=(By.ID,"genre_ids")
        self.is_series=(By.ID,"is_series")
        self.parent_id=(By.ID,"parent_id")
        self.shelf_id=(By.ID,"shelf_id")

        #publisher
        self.publisher_page=(By.XPATH,"//a[@name='publisher']")
        self.is_translated=(By.ID,"is_translated")
        self.translated_by=(By.ID,"translator_id")
        self.translated_from=(By.ID,"translated_from")
        self.translated_to=(By.ID,"translated_to")
        self.publisher_id=(By.ID,"publisher_id")
        self.date_published=(By.ID,"date_published")
        self.edition=(By.ID,"edition")
        self.pages=(By.ID,"pages")

        #description
        self.description_page=(By.XPATH,"//a[@name='description_info']")
        self.write_description=(By.ID,"description")

        self.autocomplete_dropdown = (By.CLASS_NAME, "o-autocomplete--dropdown-item")

        #save book
        self.save_icon = (By.CLASS_NAME, "fa-cloud-upload")

    def open_lms_book(self):
        try:
            lms_book=self.driver.find_element(*self.lms_member).click()
            time.sleep(2)
        except Exception as exp:
            print("Failed: Book Menuitem unable to click")
            print(exp)
        else:
            print("Success: Opened LMS Book")

    def click_new_book(self):
        try:
            new=self.driver.find_element(*self.new).click()
            time.sleep(5)
        except Exception as E:
            print("Failed: Failed to create a new author")
            print(E)
        else:
            print("Success: Created a new author")

    def fill_book_information(self,**kwargs):
        try:
            time.sleep(2)
            name = self.driver.find_element(*self.name).send_keys(kwargs.get("name"))
            isbn = self.driver.find_element(*self.isbn).send_keys(kwargs.get("isbn"))

            #author
            authors=kwargs.get("authors",[])
            for author in authors:
                author_input = self.driver.find_element(*self.author_ids).send_keys(author)
                time.sleep(2)
                author_options = self.driver.find_elements(*self.autocomplete_dropdown)
                if author_options:
                    author_options[0].click()
                time.sleep(2)

            #country
            country_input = self.driver.find_element(*self.country_id)
            country_input.send_keys(kwargs.get("country"))
            time.sleep(2)
            country_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if country_options:
                country_options[0].click()
            time.sleep(2)

            #mrp
            mrp_clear=self.driver.find_element(*self.MRPprice).clear()
            mrp=self.driver.find_element(*self.MRPprice).send_keys(kwargs.get("mrp"))

            #language
            language_input = self.driver.find_element(*self.language_id)
            language_input.send_keys(kwargs.get("language"))
            time.sleep(2)
            language_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if language_options:
                language_options[0].click()
            time.sleep(2)

            #genre
            genres=kwargs.get("genre",[])
            for genre in genres:
                genre_input = self.driver.find_element(*self.genre_ids).send_keys(genre)
                time.sleep(2)
                genre_options = self.driver.find_elements(*self.autocomplete_dropdown)
                if genre_options:
                    genre_options[0].click()
                time.sleep(2)
            
            is_series_kwargs=kwargs.get("series")
            if is_series_kwargs != False:
                series=self.driver.find_element(*self.is_series).click()
            time.sleep(2)

            #shelf
            shelf_input=self.driver.find_element(*self.shelf_id)
            shelf_input.send_keys(kwargs.get("shelf"))
            time.sleep(2)
            shelf_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if shelf_options:
                shelf_options[0].click()
            time.sleep(2)
        except Exception as E:
            print("Failed: Failed to Fill Book Information")
            print(E)
        else:
            print("Success: Filled Book Information")

    def fill_book_information_publisher(self,**kwargs):
        try:
            publisher_page=self.driver.find_element(*self.publisher_page).click()
            self.driver.implicitly_wait(2)

            #is_translated
            is_translated_kwargs=kwargs.get("is_translated")
            if is_translated_kwargs != False:
                series=self.driver.find_element(*self.is_translated).click()
            time.sleep(2)

            if (kwargs.get("is_translated")) == True:
                translated_by=self.driver.find_element(*self.translated_by).send_keys(kwargs.get("translated_by"))
                time.sleep(2)
                translated_by_options = self.driver.find_elements(*self.autocomplete_dropdown)
                if translated_by_options:
                    translated_by_options[0].click()
                    time.sleep(2)

                translated_from=self.driver.find_element(*self.translated_from).send_keys(kwargs.get("translated_from"))
                time.sleep(2)
                translated_from_options = self.driver.find_elements(*self.autocomplete_dropdown)
                if translated_from_options:
                    translated_from_options[0].click()
                    time.sleep(2)

                tanslated_to=self.driver.find_element(*self.translated_to).send_keys(kwargs.get("translated_to"))
                time.sleep(2)
                translated_to_options = self.driver.find_elements(*self.autocomplete_dropdown)
                if translated_to_options:
                    translated_to_options[0].click()
                    time.sleep(2)

            #publisher
            publisher=self.driver.find_element(*self.publisher_id).send_keys(kwargs.get("publisher"))
            time.sleep(2)
            publisher_options = self.driver.find_elements(*self.autocomplete_dropdown)
            if publisher_options:
                    publisher_options[0].click()
                    time.sleep(2)

            #date published
            date_published=self.driver.find_element(*self.date_published).send_keys(kwargs.get("date_published"))

            #edition
            edition=self.driver.find_element(*self.edition).send_keys(kwargs.get("edition"))

            #page
            page=self.driver.find_element(*self.pages).clear()
            page=self.driver.find_element(*self.pages).send_keys(kwargs.get("pages"))
            self.driver.implicitly_wait(2)
        except Exception as E:
            print("Failed: Failed to Fill Publisher Information")
            print(E)
        else:
            print("Success: Filled Publisher Information")
    
    def book_fill_information_description(self,**kwargs):
        try:
            #description
            description_page=self.driver.find_element(*self.description_page).click()
            self.driver.implicitly_wait(2)
            description=self.driver.find_element(*self.write_description).send_keys(kwargs.get("write_description"))
            time.sleep(4)
        except Exception as E:
            print("Failed: Failed to Fill Description")
            print(E)
        else:
            print("Success: Filled Description Information")

    def save_author(self):
        try:
            # save the author information
            save_icon = self.driver.find_element(*self.save_icon)
            save_icon.click()
            self.driver.implicitly_wait(2)
            time.sleep(2)
        except Exception as E:
            print("Failed: Failed To Save Book Information")
            print(E)
        else:
            print("Success: Saved Book Information")