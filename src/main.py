"""Main module of insta-mon. Containing the instagram backend logic."""
import logging
import time
from threading import Thread

from src import config, log

# Setup logging
log.setup_logging()
logger = logging.getLogger(__name__)


class InstaMon:
    """Main class for instagram backend logic."""

    def __init__(self):
        pass

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
