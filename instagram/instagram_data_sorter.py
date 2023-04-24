class DataSorter:
    def __init__(self, metadata):
        self.metadata = metadata

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
            metadata = self.metadata
            name = metadata.full_name
            username = metadata.username
            bio = metadata.biography
            is_private = metadata.is_private
            post_amount = metadata.posts.count
            follower = metadata.followers
            followings = metadata.followees
            metadata_sorted = [name, username, bio, is_private, post_amount, follower, followings]

            return metadata_sorted
        except Exception as e:
            print("An error occurred while sorting the metadata.", e)
            quit(-1)

