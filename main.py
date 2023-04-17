"""
    Python script for tracking and recording activity of a single Instagram account.

    /*Changes
    * Made the script new from scratch.
    */

    V0.10 <--> 17.04.2023
"""

import instaloader


class InstaMon:
    def __init__(self):
        self.settings_input = SettingsInput()

    def main(self):
        """
        Function that executes the modules of the script.
        :return: None
        """
        target_username = self.settings_input.select_target_username()
        user_login_details = self.settings_input.select_login_details()

        instagram_scraper = InstagramScraper(target_username, user_login_details)

        instagram_scraper.get_metadata()
        instagram_scraper.get_profile_picture_url()
        instagram_scraper.get_posts()


class SettingsInput:
    @staticmethod
    def select_target_username():
        target_username = input("Enter target username: ")
        return target_username

    @staticmethod
    def select_login_details():
        login_details = input("Enter login details: ")
        return login_details


class InstagramScraper:
    def __init__(self, target, user):
        self.target = target
        self.user = user
        self.bot = instaloader.Instaloader()
        self.profile = instaloader.Profile.from_username(self.bot.context, self.target)

    def get_metadata(self):
        try:
            profile_metadata = self.profile.get_metadata()
            return profile_metadata
        except Exception as e:
            print("Something went wrong during the metadata request.", e)

    def get_profile_picture_url(self):
        try:
            profile_picture = self.profile.get_profile_pic_url()
            return profile_picture
        except Exception as e:
            print("Something went wrong during the profile picture url request.", e)

    def get_posts(self):
        try:
            if not self.profile.is_private:
                posts = self.profile.get_posts()
                return posts
        except Exception as e:
            print("Something went wrong during the get post request.", e)


if __name__ == "__main__":
    app = InstaMon()
    app.main()
