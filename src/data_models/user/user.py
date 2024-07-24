"""
Defines the User data class with attributes and methods for managing Instagram user data.
"""


class User:
    """Class representing an Instagram user."""

    def __init__(self, uid: str, username: str, name: str, bio: str, post_amount: int,
                 follower_amount: int, follows_amount: int):
        """
        Initialize a new User instance.

        Args:
            uid (str): The Instagram user id.
            username (str): The user's Instagram username.
            name (str): The user's full name.
            bio (str): The user's biography.
            post_amount (int): The number of posts the user has made.
            follower_amount (int): The number of followers the user has.
            follows_amount (int): The number of users this user follows.
        """
        self.uid = uid
        self.username = username
        self.name = name
        self.bio = bio
        self.post_amount = post_amount
        self.follower_amount = follower_amount
        self.follows_amount = follows_amount

    def __repr__(self) -> str:
        """
        Return a string representation of the User instance.

        Returns:
            str: A string representation of the user.
        """
        return (
            f"User(uid={self.uid}, username={self.username}, name={self.name}, bio={self.bio},"
            f" post_amount={self.post_amount}, follower_amount={self.follower_amount},"
            f" follows_amount={self.follows_amount})")

    def set_uid(self, new_uid: str) -> None:
        """
        Set the user's uid.

        Args:
            new_uid (str): The new uid.
        """
        self.uid = new_uid

    def get_uid(self) -> str:
        """
        Get the user's uid.

        Returns:
            str: The current uid of the user.
        """
        return self.uid

    def set_username(self, new_username: str) -> None:
        """
        Set the user's username.

        Args:
            new_username (str): The new username.
        """
        self.username = new_username

    def get_username(self) -> str:
        """
        Get the user's username.

        Returns:
            str: The current username of the user.
        """
        return self.username

    def set_name(self, new_name: str) -> None:
        """
        Set the user's name.

        Args:
            new_name (str): The new name.
        """
        self.name = new_name

    def get_name(self) -> str:
        """
        Get the user's name.

        Returns:
            str: The current name of the user.
        """
        return self.name

    def set_bio(self, new_bio: str) -> None:
        """
        Set the user's bio.

        Args:
            new_bio (str): The new biography.
        """
        self.bio = new_bio

    def get_bio(self) -> str:
        """
        Get the user's bio.

        Returns:
            str: The current biography of the user.
        """
        return self.bio

    def set_post_amount(self, new_post_amount: int) -> None:
        """
        Set the user's post amount.

        Args:
            new_post_amount (int): The new post amount.
        """
        self.post_amount = new_post_amount

    def get_post_amount(self) -> int:
        """
        Get the user's post amount.

        Returns:
            int: The current post amount of the user.
        """
        return self.post_amount

    def set_follower_amount(self, new_follower_amount: int) -> None:
        """
        Set the user's follower amount.

        Args:
            new_follower_amount (int): The new follower amount.
        """
        self.follower_amount = new_follower_amount

    def get_follower_amount(self) -> int:
        """
        Get the user's follower amount.

        Returns:
            int: The current follower amount of the user.
        """
        return self.follower_amount

    def set_follows_amount(self, new_follows_amount: int) -> None:
        """
        Set the user's follows amount.

        Args:
            new_follows_amount (int): The new follows amount.
        """
        self.follows_amount = new_follows_amount

    def get_follows_amount(self) -> int:
        """
        Get the user's follows amount.

        Returns:
            int: The current follows amount of the user.
        """
        return self.follows_amount
