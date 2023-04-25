from instaloader import instaloader


class InstagramHandler:
    def __init__(self, target_name):
        try:
            self.bot = instaloader.Instaloader()
            self.profile = instaloader.Profile.from_username(self.bot.context, target_name)
        except instaloader.LoginRequiredException as lre:
            print("Please login to your Instagram account. Or wait a few minutes and try again.", lre)
            quit(-1)
        except Exception as e:
            print("An error occurred while communicating with the Instagram API.", e)
            quit(-1)
        