"""
Defines the Reel data class with attributes and methods for managing Instagram reel data.
"""


class Reel:
    """Class representing an Instagram reel post."""
    def __init__(self, video_path: str, description: str, like_amount: str, comment_amount: str):
        # TODO: add comments, likes
        """
        Initialize a new Reel post instance.

        Args:
            video_path (str): The Instagram reel post path.
            description (str): The Instagram reel post description.
            like_amount (str): The Instagram reel post amount of likes .
            comment_amount (str): The Instagram reel post amount of comments .

        """
        self.reel_path = video_path
        self.description = description
        self.like_amount = like_amount
        self.comment_amount = comment_amount

    def __repr__(self) -> str:
        """
        Return a string representation of the Reel instance.

        Returns:
            str: A string representation of the reel.
        """
        return (
            f"Reel(reel_path={self.reel_path}, description={self.description}, "
            f"like_amount={self.like_amount}, comment_amount={self.comment_amount}"
        )

    def set_reel_path(self, new_path: str) -> None:
        """
        Set the reel post path.

        Args:
            new_path (str): The new path.
        """
        self.reel_path = new_path

    def get_reel_path(self) -> str:
        """
        Get the reel post path.

        Returns:
            str: The current path of the reel.
        """
        return self.reel_path

    def set_description(self, new_description: str) -> None:
        """
        Set the description.

        Args:
            new_description (str): The new description.
        """
        self.description = new_description

    def get_description(self) -> str:
        """
        Get the description of the post.

        Returns:
            str: The current description.
        """
        return self.description

    def set_like_amount(self, set_like_amount: str) -> None:
        """
        Set the like amount.

        Args:
            set_like_amount (str): The new amount.
        """
        self.like_amount = set_like_amount

    def get_like_amount(self) -> str:
        """
        Get the posts like amount.

        Returns:
            str: The current like amount.
        """
        return self.like_amount

    def set_comment_amount(self, new_comment_amount: str) -> None:
        """
        Set the posts comment amount.

        Args:
            new_comment_amount (str): The new comment amount.
        """
        self.comment_amount = new_comment_amount

    def get_comment_amount(self) -> str:
        """
        Get the post comment amount.

        Returns:
            str: The current comment amount.
        """
        return self.comment_amount
