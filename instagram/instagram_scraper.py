from pathlib import Path
from instagram.instagram_handler import InstagramHandler


class InstagramScraper:
    def __init__(self, target_name):
        self.target_name = target_name
        self.instagram_handler = InstagramHandler(target_name)

    def get_metadata(self):
        """
        Function that scraps the metadata of a user.
        :return: metadata
        """
        try:
            metadata = self.instagram_handler.profile
            return metadata
        except Exception as e:
            print("An error occurred while getting metadata.", e)
            quit(-1)

    def get_profile_picture_url(self):
        """
        Function that scraps the profile picture url of a user.
        :return: profile_picture_url
        """
        try:
            profile_picture_url = self.instagram_handler.profile.get_profile_pic_url()
            return profile_picture_url
        except Exception as e:
            print("An error occurred while getting the profile picture url.", e)
            quit(-1)

    def get_profile_picture(self):
        """
        Function that downloads and saves the profile picture of a user.
        """
        try:
            profile = self.instagram_handler.profile
            picture_url = self.get_profile_picture_url()
            target_name = self.target_name
            path = Path(target_name + '/profile_pictures')
            self.instagram_handler.bot.download_title_pic(picture_url, path, 'profile_picture', profile)
        except Exception as e:
            print("An error occurred while downloading or saving the profile picture.", e)
            quit(-1)

    def get_posts(self):
        """
        Function that scraps the posts of a user.
        :return: posts
        """
        try:
            posts = self.instagram_handler.profile.get_posts()
            return posts
        except Exception as e:
            print("An error occurred while getting posts.", e)
            quit(-1)
