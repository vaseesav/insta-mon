import logging


class LogController:
    """Handles the log messages"""

    def __init__(self, cls_name):
        handler = logging.FileHandler('insta-mon.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        self.logger = logging.getLogger(cls_name)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(handler)

