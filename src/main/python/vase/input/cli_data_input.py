import argparse


class DataInput:
    def __init__(self):
        self.target_id = None
        self.login_data = None
        self.stop_date = None

    def get_target_id(self):
        return self.target_id

    def get_login_data(self):
        return self.login_data

    def get_stop_date(self):
        return self.stop_date

    @staticmethod
    def args_parser():
        """
        Function that parses arguments from the command line.
        :return: args: arguments from the command line
        """

        try:
            parser = argparse.ArgumentParser()
            parser.add_argument("-t", "--target", help="Target id", required=True)
            parser.add_argument("-l", "--login", help="Login data username:pass", required=False)
            parser.add_argument("-s", "--stop", help="Date to stop scraping.", required=False)
            args = parser.parse_args()

            if args is not None:
                return args
            else:
                return None
        except Exception as e:
            print("An error occurred while parsing the start arguments.", e)
            quit(-1)

    def set_target_id(self):
        """Function that sets the target_id"""

        try:
            args = self.args_parser()
            target_id = args.target
            self.target_id = target_id
        except Exception as e:
            print("An error occurred while setting the target_id", e)

    def set_login_data(self):
        """Function that sets the login_data"""

        try:
            args = self.args_parser()
            login_data = args.login
            login_data = str(login_data).split(':')
            self.login_data = login_data
        except Exception as e:
            print("An error occurred while setting the login_data", e)

    def set_stop_date(self):
        """Function that sets the stop_date"""

        try:
            args = self.args_parser()
            stop_date = args.stop
            self.stop_date = stop_date
        except Exception as e:
            print("An error occurred while setting the stop_date", e)

    def data_input(self):
        self.args_parser()
        self.set_login_data()
        self.set_stop_date()
        self.set_target_id()
