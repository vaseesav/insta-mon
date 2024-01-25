"""Insta-mon Insta module with login functionality."""

import logging
from typing import Optional

from instagrapi import Client


class InstaLoginException(Exception):
    """Custom exception for Insta login-related errors."""
    # TODO: implement


class InstaLogin:
    """Handles the Insta login process."""

    def __init__(self) -> None:
        self.client: Optional[Client] = None

        logging.basicConfig(
            filename='insta_login.log',
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def perform_login(self, username: str, password: str, verification_code: Optional[str] = None) -> bool:
        """
        Attempts to log in to Insta using provided credentials.

        Args:
            username: Insta username.
            password: Insta password
            verification_code: Verification code if two-factor authentication is enabled

        Returns:
            True if login is successful, False otherwise.

        Raises:
            InstaLoginException: If login fails due to specific errors.
        """

        try:
            if not self.client:
                self.client = Client()

            if verification_code:
                self.client.login(username, password, verification_code=verification_code)
            else:
                self.client.login(username, password)

            logging.info("Login successful for user: %s", username)
            return True

        except self.client.handle_exception as e:
            logging.error("Login failed: %s", str(e))
            raise InstaLoginException(f"Login failed due to Insta error: {e}") from e
        except Exception as e:
            logging.error("Login failed: %s", str(e))
            raise InstaLoginException("An unexpected error occurred during login.") from e
