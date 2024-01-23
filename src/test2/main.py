class InstaMon:
    def __init__(self):
        # Parsing the start arguments
        cli_data_input = src.test2.input.cli_data_input.DataInput()
        cli_data_input.data_input()
        self.target_id = cli_data_input.get_target_id()
        self.login_data = cli_data_input.get_login_data()
        self.stop_date = cli_data_input.get_stop_date()

        # Parsing the arguments to the db
        target_data_db_operations = src.test2.db.target_data_db_operations.CreateTargetDatabase(str(self.target_id))
        target_data_db_operations.create_tables()

    def main(self):
        pass


if __name__ == "__main__":
    app = InstaMon()
    app.main()
