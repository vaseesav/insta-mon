from instaloader import instaloader


class InstagramHandler:
    def __int__(self, target_name):
        self.bot = instaloader.Instaloader()
        self.profile = instaloader.Profile.from_username(self.bot.context, target_name)
        