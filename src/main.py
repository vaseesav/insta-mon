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

    def insta_scrap_query_handler(self) -> None:
        """
        Function which periodically scrapes instagram data of a certain user from instagram API.

        :return: None
        """
        first_run = True
        ACCOUNT_USERNAME = self.args.username
        ACCOUNT_PASSWORD = self.args.password

        try:
            if ACCOUNT_USERNAME and ACCOUNT_PASSWORD:
                self.client.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)
        except instagrapi.exceptions.BadPassword as password_error:
            logger.error("The password is wrong: %s", password_error)
        except instagrapi.exceptions.ReloginAttemptExceeded as exceeded_error:
            logger.error("Too many failed login attempts %s", exceeded_error)
        except instagrapi.exceptions.ChallengeRequired as challenge_error:
            logger.error("Challenge is required: %s", challenge_error)
        except Exception as error:
            logger.error("An  unexpected error occurred while trying to log "
                         "into instagram: %s", error)

        while True:
            if not first_run:
                time.sleep(config.get("SCRAP_INTERVAL"))
            first_run = False

            logger.debug('Run completed!')


class ArgumentParser:
    """Class which handles the argument parsing."""
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Instamon settings.')
        self.parser.add_argument('-u', '--username', type=str, required=False,
                                 help='The username for the account to log into')
        self.parser.add_argument('-p', '--password', type=str, required=False,
                                 help='The password for the account to log into')
        self.parser.add_argument('-t', '--tfa', type=str, required=False,
                                 help='The 2FA code for the account to log into')
        self.parser.add_argument('-s', '--sessionid', type=str, required=False,
                                 help='The session id for the account to log into')

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
