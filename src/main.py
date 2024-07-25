"""Main module of insta-mon. Containing the instagram backend logic."""
import argparse
import logging
import time

from src import config, log

# Setup logging
log.setup_logging()
logger = logging.getLogger(__name__)


class InstaMon:
    """Main class for instagram backend logic."""

    def __init__(self):
        self.arg_parser = ArgumentParser()
        self.args = self.arg_parser.parse_arguments()

    def insta_scrap_query_handler(self) -> None:
        """
        Function which periodically scrapes instagram data of a certain user from instagram API.

        :return: None
        """
        first_run = True
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
