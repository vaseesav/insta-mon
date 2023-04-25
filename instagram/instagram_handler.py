from instaloader import instaloader
from logger.logger_handler import LoggingHandler


class InstagramHandler:
    def __init__(self, target_name):
        try:
            self.logger = LoggingHandler(self.__class__.__name__).logger
            self.logger.info("Loging in to Instagram.")
            self.bot = instaloader.Instaloader()
            self.profile = instaloader.Profile.from_username(self.bot.context, target_name)
        except instaloader.LoginRequiredException as lre:
            print("Please login to your Instagram account. Or wait a few minutes and try again.", lre)
            self.logger.critical("Failed to reach account page. Please login!")
            quit(-1)
        except Exception as e:
            print("An error occurred while communicating with the Instagram API.", e)
            self.logger.critical("Failed to reach Instagram or Instagram account is not valid.", e)
            quit(-1)
        