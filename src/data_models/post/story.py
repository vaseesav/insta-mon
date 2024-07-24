"""
Defines the Story data class with attributes and methods for managing Instagram story data.
"""


class Story:
    """Class representing an Instagram Story post."""
    def __init__(self, media_path: str):
        """
        Initialize a new Story post instance.

        Args:
            media_path (str): The Instagram Story post path.
        """
        self.story_path = media_path

    def __repr__(self) -> str:
        """
        Return a string representation of the Story instance.

        Returns:
            str: A string representation of the Story.
        """
        return f"Story(story_path={self.story_path}"

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
