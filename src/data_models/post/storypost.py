"""
Defines the Story data class with attributes and methods for managing Instagram story data.
"""

from src.data_models.post.post import Post


class StoryPost(Post):
    """Class representing an Instagram Story post."""

    def __init__(self, post_id: str, media_path: str):
        """
        Initialize a new Story post instance.

        Args:
            media_path (str): The Instagram Story post path.
        """
        super().__init__(
            post_id=post_id,
            post_type="Story",
            media_path=media_path,
            description="",
            like_amount="",
            comment_amount=""
        )
        self.post_id = post_id
        self.story_path = media_path

    def __repr__(self) -> str:
        """
        Return a string representation of the Story instance.

        Returns:
            str: A string representation of the Story.
        """
        return f"Story(post_id={self.post_id}, story_path={self.story_path}"

    def set_post_id(self, new_id: str) -> None:
        """
        Set the picture post path.

        Args:
            new_id (str): The new id.
        """
        self.post_id = new_id

    def set_story_path(self, new_path: str) -> None:
        """
        Set the Story post path.

        Args:
            new_path (str): The new path.
        """
        self.story_path = new_path

    def get_story_path(self) -> str:
        """
        Get the Story post path.

        Returns:
            str: The current path of the Story.
        """
        return self.story_path
