from .genre_setup import LMSGenre
import random,os
from dotenv import load_dotenv
load_dotenv()

class LMSGenreTest:
    def __init__(self, driver):
        self.driver = driver

    color_choices = os.getenv("LMSGenre_COLOR").split(',')
    random_choice = random.choice(color_choices)
    genre_details = {
        "name": os.getenv("LMSGenre_NAME"),
        "choice": random_choice
    }

    def genre_creation(self):
        lms_genre = LMSGenre(self.driver)
        lms_genre.open_lms_genre()
        lms_genre.new_genre(**self.genre_details)
        lms_genre.save_genre()
