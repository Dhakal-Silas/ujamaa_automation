from .issue_setup import LMSBookIssue
from .return_setup import LMSBookReturn
import os
from dotenv import load_dotenv
load_dotenv()

class LMSBookIssueTest:
    def __init__(self, driver):
        self.driver = driver

    issue_details = {
        "member": os.getenv("LMSIssue_MEMBER"),
        "book": os.getenv("LMSIssue_BOOK"),
        "issued_date": os.getenv("LMSIssue_IssueDate"),
    }

    def book_issue_creation(self):
        lms_book_issue=LMSBookIssue(self.driver)
        lms_book_issue.open_LMSBook_Issue()
        lms_book_issue.IssueaBook(**self.issue_details)
        # lms_book_issue.ResetButton()
        lms_book_issue.IssueButton()

    def book_return(self):
        lms_book_return=LMSBookReturn(self.driver)
        lms_book_return.open_LMSBook_Issue()
        lms_book_return.open_issue_history()
        lms_book_return.search_book(**self.issue_details)
        lms_book_return.find_return_book()


