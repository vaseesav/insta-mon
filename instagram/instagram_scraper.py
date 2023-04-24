from instagram.instagram_handler import InstagramHandler


class InstagramScraper:
    def __int__(self, target_name):
        self.target_name = target_name
        self.instagram_handler = InstagramHandler()

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
        pass

    def get_profile_picture(self):
        pass

    def get_posts(self):
        pass
