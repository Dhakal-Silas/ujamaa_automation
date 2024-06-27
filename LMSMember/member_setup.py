from selenium.webdriver.common.by import By
import time

class LMSMembers:
    def __init__(self,driver):    
        self.driver=driver  

        # LMS member menuitem
        self.lms_member = (By.XPATH, "//a[@data-menu-xmlid='lms_member.lms_member_menu']")

        #NEW
        self.new=(By.XPATH, "//button[@class='btn btn-primary o-kanban-button-new']")

        #Member Fields
        self.name=(By.ID,"member_name")
        self.address=(By.ID,"address")
        self.phone_no=(By.ID,"phone_no")
        self.date_of_birth=(By.ID,"date_of_birth")
        self.member_email=(By.ID,"email")
        self.membership_type=(By.ID,"membership_type")
        self.membership_price=(By.ID,"membership_price")
        self.payment_status=(By.ID,"payment_status")
        self.partial_payment_amount=(By.ID,"partially_paid_amount")
        self.issued_date=(By.ID,"issued_date")
        self.expiry_date=(By.ID,"expiry_date")

        # Save Information
        self.save_icon = (By.CLASS_NAME, "fa-cloud-upload")

    def open_lms_member(self):
        try:
            lms_member=self.driver.find_element(*self.lms_member).click()
            time.sleep(2)
        except Exception as exp:
            print("Failed: App unable to click")
            print(exp)
        else:
            print("Success: Open LMS Member")
    
    def new_member(self,**kwargs):
        try:
            new=self.driver.find_element(*self.new).click()

            name = self.driver.find_element(*self.name).send_keys(kwargs.get("name"))
            phone_no = self.driver.find_element(*self.phone_no).send_keys(kwargs.get("phone_no"))
            address = self.driver.find_element(*self.address).send_keys(kwargs.get("address"))
            date_of_birth = self.driver.find_element(*self.date_of_birth).send_keys(kwargs.get("date_of_birth"))
            email = self.driver.find_element(*self.member_email).send_keys(kwargs.get("member_email"))
            membership_type = self.driver.find_element(*self.membership_type).send_keys(kwargs.get("membership_type"))
            membership_price_clear = self.driver.find_element(*self.membership_price).clear()
            membership_price = self.driver.find_element(*self.membership_price).send_keys(kwargs.get("membership_price"))
            payment_status = self.driver.find_element(*self.payment_status).send_keys(kwargs.get("payment_status"))
            if (kwargs.get("payment_status")) == "Partially Paid":
                partial_payment_clear = self.driver.find_element(*self.partial_payment_amount).clear()
                partial_payment_amount=self.driver.find_element(*self.partial_payment_amount).send_keys(kwargs.get("partial_paid_amount"))
            issued_date = self.driver.find_element(*self.issued_date).send_keys(kwargs.get("issued_date"))
            expiry_date = self.driver.find_element(*self.expiry_date).send_keys(kwargs.get("expiry_date"))
            time.sleep(5)
        except Exception as E:
            print("Failed: Failed to create a new member")
            print(E)
        else:
            print("Success: Created a new member")

    def save_member(self):
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
            print("Success: Saved Member Information")
