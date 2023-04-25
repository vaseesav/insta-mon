import logging


class LoggingHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.handler = logging.FileHandler('insta-mon.log')
        self.handler.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.DEBUG)
        self.format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.format)
        self.logger.addHandler(self.handler)
