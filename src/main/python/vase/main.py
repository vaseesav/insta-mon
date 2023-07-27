import input.cli_data_input


class InstaMon:
    def __init__(self):
        # "Links"
        cli_data_input = input.cli_data_input.DataInput()

        # Parsing the start arguments
        cli_data_input.data_input()
        self.target_id = cli_data_input.get_target_id()
        self.login_data = cli_data_input.get_login_data()
        self.stop_date = cli_data_input.get_stop_date()

    def main(self):
        pass


if __name__ == "__main__":
    app = InstaMon()
    app.main()
