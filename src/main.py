"""Main module of insta-mon. Containing the instagram backend logic."""
import argparse
import logging
import time

import instagrapi.exceptions

from src import config, log
from instagrapi import Client


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
        return self.client.user_info_by_username(username=target_username, use_cache=False)

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
            target_user_info = self.get_user_info(target_username=TARGET_USERNAME)
            print(target_user_info)
            logger.debug('Run completed!')


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
