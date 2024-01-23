import logging


class LoggingHandler:
    def __init__(self, cls_name):
        self.logger = logging.getLogger(cls_name)
        self.handler = logging.FileHandler('login_and_data_fetcher.py-mon.log')
        self.logger.setLevel(logging.DEBUG)
        self.format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.format)
        self.logger.addHandler(self.handler)


