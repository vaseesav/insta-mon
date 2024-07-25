"""Module base for posts"""


class Post:
    """Base class for different types of posts."""

    def __init__(self, post_id: str, post_type: str, media_path: str, description: str,
                 like_amount: int, comment_amount: int):
        self.post_id = post_id
        self.post_type = post_type
        self.media_path = media_path
        self.description = description
        self.like_amount = like_amount
        self.comment_amount = comment_amount

    def to_tuple(self) -> tuple:
        """Convert the base post attributes to a tuple for database insertion."""
        return (self.post_id, self.post_type, self.media_path, self.description, self.like_amount,
                self.comment_amount)
