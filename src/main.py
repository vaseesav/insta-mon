"""Main module of insta-mon. Containing the instagram backend logic."""
from threading import Thread


class InstaMon:
    """Main class for instagram backend logic."""
    def __init__(self):
        pass

    def insta_scrap_query_handler(self) -> None:
        """
        Function which periodically scrapes instagram data of a certain user from instagram API.

        :return: None
        """
        pass


if __name__ == "__main__":
    app = InstaMon()
    insta_scrap_thread = Thread(target=app.insta_scrap_query_handler)
    insta_scrap_thread.daemon = True
    insta_scrap_thread.start()
