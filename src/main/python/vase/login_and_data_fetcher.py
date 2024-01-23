"""Insta-mon Insta module

This module handles the Instagram login process,
retrieves data from the user's profile, and transforms it into a structured format.
"""

from instagrapi import Client


class InstagramLogin:
    """
    Class that handles the Insta login process
    """

    def __init__(self):
        self.client = None
        self.username = None
        self.password = None

    def login(self, username, password, verification_code=None):
        self.client = Client()

        if verification_code is not None:
            self.client.login(username, password, verification_code=verification_code)
        else:
            self.client.login(username, password)

        self.username = username
        self.password = password

