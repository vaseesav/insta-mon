from logger.logger_handler import LoggingHandler


class DataSorter:
    def __init__(self, metadata, user_post_data):
        self.metadata = metadata
        self.user_post_data = user_post_data
        self.logger = LoggingHandler().logger

    def get_metadata(self):
        """
        Function that returns the sorted metadata.
        :return: metadata_sorted
        """
        return self.sort_metadata()

    def sort_metadata(self):
        """
        Function that sorts the metadata into a db_inserter suitable format.
        :return: metadata_sorted
        """
        try:
            self.logger.info("Sorting the metadata...")
            metadata = self.metadata
            post_data = self.user_post_data
            name = metadata.full_name
            username = metadata.username
            bio = metadata.biography
            is_private = metadata.is_private
            post_amount = post_data.count
            follower = metadata.followers
            followings = metadata.followees
            metadata_sorted = [name, username, bio, is_private, post_amount, follower, followings]

            return metadata_sorted
        except Exception as e:
            print("An error occurred while sorting the metadata.", e)
            self.logger.error("An error occurred while sorting the metadata", e)
            quit(-1)

