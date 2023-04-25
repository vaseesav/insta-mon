import argparse

from logger.logger_handler import LoggingHandler


class DataInput:
    def __init__(self):
        self.logger = LoggingHandler(self.__class__.__name__).logger

    @staticmethod
    def get_target_username():
        target_username = input('Enter target username: ')
        return target_username

    def get_arguments(self):
        """
        Function that gets the arguments from the command line.
        :return: args
        """
        try:
            self.logger.info("Parsing arguments.")
            parser = argparse.ArgumentParser()
            parser.add_argument("-t", "--target", help="Target username", required=True)
            args = parser.parse_args()
            if args.target is not None:
                return args
        except Exception as e:
            print("An error occurred while parsing the arguments.", e)
            self.logger.error("An error occurred while parsing the arguments.")
            quit(-1)

    def get_target_username_args(self):
        """
        Function that gets the target_username from the args.
        :return: target_username
        """
        try:
            args = self.get_arguments()
            target_username = args.target
            return str(target_username)
        except Exception as e:
            print("An error occurred while parsing the target_username.", e)
            self.logger.error("An error occurred while parsing the target_username.")
            quit(-1)
