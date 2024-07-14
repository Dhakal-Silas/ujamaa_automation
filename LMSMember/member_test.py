from .member_setup import LMSMembers
import random,os
from dotenv import load_dotenv
load_dotenv()

class LMSMemberTest:
    def __init__(self, driver):
        self.driver = driver
        
    members_info = {
        "name": os.getenv("LMSMember_NAME"),
        "phone_no": os.getenv("LMSMember_PHONE_NO"),
        "address": os.getenv("LMSMember_ADDRESS"),
        "date_of_birth": os.getenv("LMSMember_DATE_OF_BIRTH"),
        "member_email": os.getenv("LMSMember_MEMBER_EMAIL"),
        "membership_type": random.choice(["Silver", "Gold", "Premium"]),
        "membership_price": str(random.uniform(1000, 2000)),
        "payment_status": random.choice(["Paid", "Unpaid","Partially Paid"]),
        "partial_paid_amount": str(random.uniform(100, 500)),
        "issued_date": os.getenv("LMSMember_ISSUED_DATE"),
        "expiry_date": os.getenv("LMSMember_EXPIRY_DATE")
    }

    def member_creation(self):
        lms_members = LMSMembers(self.driver)
        lms_members.open_lms_member()
        lms_members.new_member(**self.members_info)
        lms_members.save_member()


