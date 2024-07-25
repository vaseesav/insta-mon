"""Main module of insta-mon. Containing the instagram backend logic."""
import argparse
import logging
import os
import time
from io import BytesIO
from urllib.parse import urlparse

import instagrapi.exceptions
import requests
from PIL import Image
from instagrapi import Client

from src import config, log
from src.data_models import User
from src.db import insert_user

# Setup logging
log.setup_logging()
logger = logging.getLogger(__name__)


class InstaMon:
    """Main class for instagram backend logic."""

    def __init__(self):
        self.arg_parser = ArgumentParser()
        self.args = self.arg_parser.parse_arguments()
        self.client = Client()

    def get_user_info(self, target_username: str) -> object:
        """
        Function to get user info from instagram.

        :param target_username: instagram username
        :return: instagram user info
        """
        return self.client.user_info_by_username(username=target_username, use_cache=False)

    def download_image(self, url: str, target_type: str) -> str:
        """
        Downloads an image from the provided URL and saves it to a specified directory.

        :param url: The URL of the image to be downloaded.
        :param target_type: The target directory type, either 'profilePicture' or 'post'.

        :return: The path where the image is saved.

        :raises ValueError: If the target_type is not 'profilePicture' or 'post'.
        :raises requests.exceptions.RequestException: If there is an issue with the HTTP request.
        :raises OSError: If there is an issue creating directories or saving the file.
        """

        if target_type not in ['profilePicture', 'post']:
            raise ValueError("target_type must be either 'profilePicture' or 'post'")

        # Parse the URL to extract the file name
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)

        # Set the target directory
        target_dir = os.path.join('target', target_type)
        os.makedirs(target_dir, exist_ok=True)

        # Full path to save the image
        file_path = os.path.join(target_dir, file_name)

        try:
            # Send HTTP request to download the image
            response = requests.get(url, timeout=config.get("TIMEOUT_SEC"))
            response.raise_for_status()

            # Open the image from the response content
            image = Image.open(BytesIO(response.content))

            # Save the image using Pillow
            image.save(file_path)
        except requests.exceptions.RequestException as request_error:
            logger.error("Failed to download image from url: %s with error: %s", url, request_error)
        except OSError as e:
            logger.error("Failed to save image from url: %s with error: %s", url, e)
        return file_path

    def create_user_obj(self, target_user: instagrapi.types.User) -> User:
        """
        Function to create an instagram user object.

        :param target_user: user scraped from instagram

        :return: user object for db
        """
        uid = target_user.pk
        username = target_user.username
        name = target_user.full_name
        bio = target_user.biography
        post_amount = target_user.media_count
        follower_amount = target_user.follower_count
        follows_amount = target_user.following_count
        profile_image_path = self.download_image(str(target_user.profile_pic_url_hd), 'profilePicture')

        parsed_target_user = User(uid=uid,
                                  username=username,
                                  name=name,
                                  bio=bio,
                                  post_amount=post_amount,
                                  follower_amount=follower_amount,
                                  follows_amount=follows_amount,
                                  profile_image_path=profile_image_path)

        return parsed_target_user

    def insta_scrap_query_handler(self) -> None:
        """
        Function which periodically scrapes instagram data of a certain user from instagram API.

        :return: None
        """
        first_run = True
        ACCOUNT_USERNAME = self.args.username
        ACCOUNT_PASSWORD = self.args.password
        SECOND_FACTOR_CODE = self.args.tfa
        TARGET_USERNAME = self.args.target

        try:
            if ACCOUNT_USERNAME and ACCOUNT_PASSWORD:
                self.client.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
            elif ACCOUNT_USERNAME and ACCOUNT_PASSWORD and SECOND_FACTOR_CODE:
                self.client.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD, SECOND_FACTOR_CODE)
        except instagrapi.exceptions.BadPassword as password_error:
            logger.error("The password is wrong: %s", password_error)
        except instagrapi.exceptions.ReloginAttemptExceeded as exceeded_error:
            logger.error("Too many failed login attempts %s", exceeded_error)
        except instagrapi.exceptions.ChallengeRequired as challenge_error:
            logger.error("Challenge is required: %s", challenge_error)
        except Exception as error:
            logger.error("An unexpected error occurred while trying to log "
                         "into instagram: %s", error)

        while True:
            if not first_run:
                time.sleep(config.get("SCRAP_INTERVAL"))
            first_run = False
            target_user = self.get_user_info(target_username=TARGET_USERNAME)
            new_target_user = self.create_user_obj(target_user=target_user)
            insert_user(new_target_user)

            logger.info('Run completed!')


class ArgumentParser:
    """Class which handles the argument parsing."""

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Instamon settings.')
        self.parser.add_argument('-u', '--username', type=str, required=False,
                                 help='The username for the account to log into')
        self.parser.add_argument('-p', '--password', type=str, required=False,
                                 help='The password for the account to log into')
        self.parser.add_argument('-f', '--tfa', type=str, required=False,
                                 help='The 2FA code for the account to log into')
        self.parser.add_argument('-s', '--sessionid', type=str, required=False,
                                 help='The session id for the account to log into')
        self.parser.add_argument('-t', '--target', type=str, required=True,
                                 help='The account name of the target')

    def parse_arguments(self):
        """Function which parses arguments passed from the command line."""
        return self.parser.parse_args()


if __name__ == "__main__":
    app = InstaMon()
    # insta_scrap_thread = Thread(target=app.insta_scrap_query_handler)
    # insta_scrap_thread.daemon = False
    # insta_scrap_thread.start()

    try:
        # wait for the insta_scrap_thread to complete
        # insta_scrap_thread.join()
        app.insta_scrap_query_handler()
    except KeyboardInterrupt:
        logger.info("Shutting down.")
