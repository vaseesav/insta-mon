"""
Defines the Image data class with attributes and methods for managing Instagram image data.
"""

from src.data_models.post.post import Post


class ImagePost(Post):
    """Class representing an Instagram image post."""

    def __init__(self, post_id: str, picture_path: str, description: str,
                 like_amount: int, comment_amount: int):
        # TODO: add comments, likes
        """
        Initialize a new Image post instance.

        Args:
            post_id (str): The instagram post id.
            picture_path (str): The Instagram picture post path.
            description (str): The Instagram picture post description.
            like_amount (int): The Instagram picture post amount of likes .
            comment_amount (int): The Instagram picture post amount of comments .

        """
        super().__init__(
            post_id=post_id,
            post_type="Image",
            media_path=picture_path,
            description=description,
            like_amount=like_amount,
            comment_amount=comment_amount
        )
        self.post_id = post_id
        self.picture_path = picture_path
        self.description = description
        self.like_amount = like_amount
        self.comment_amount = comment_amount

    def __repr__(self) -> str:
        """
        Return a string representation of the Image instance.

        Returns:
            str: A string representation of the image.
        """
        return (
            f"Image(post_id={self.post_id}, picture_path={self.picture_path}, "
            f"description={self.description}, "
            f"like_amount={self.like_amount}, comment_amount={self.comment_amount}"
        )

    def set_post_id(self, new_id: str) -> None:
        """
        Set the picture post path.

        Args:
            new_id (str): The new id.
        """
        self.post_id = new_id

    def set_picture_path(self, new_path: str) -> None:
        """
        Set the picture post path.

        Args:
            new_path (str): The new path.
        """
        self.picture_path = new_path

    def get_picture_path(self) -> str:
        """
        Get the picture post path.

        Returns:
            str: The current path of the picture.
        """
        return self.picture_path

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
