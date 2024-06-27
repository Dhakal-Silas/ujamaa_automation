from .member_setup import LMSMembers
import random,os
from dotenv import load_dotenv
load_dotenv()

class LMSMemberTest:
    def __init__(self, driver):
        self.driver = driver
        
    members_info = {
        "name": "Hari Ram",
        "phone_no": "9800000000",
        "address": "Sankhamul,Kathmandu",
        "date_of_birth": "1990-01-01" ,
        "member_email": "hariram@gmail.com",
        "membership_type": random.choice(["Silver", "Gold", "Premium"]),
        "membership_price": str(random.uniform(1000, 2000)),
        "payment_status": random.choice(["Paid", "Unpaid","Partially Paid"]),
        "partial_paid_amount": str(random.uniform(100, 500)),
        "issued_date": "2000-01-01",
        "expiry_date": "2001-01-01"
    }

    def member_creation(self):
        lms_members = LMSMembers(self.driver)
        lms_members.open_lms_member()
        lms_members.new_member(**self.members_info)
        lms_members.save_member()


