from database.db_creator import DbCreator
from input.data_input import DataInput


class InstaMon:
    def __init__(self):
        self.target_name = DataInput().get_target_username()
        self.db_name = self.target_name + "-data.db"
        self.db_creator = DbCreator(self.db_name)

    def main(self):
        # Create database and its tables
        self.db_creator.create_tables()


if __name__ == "__main__":
    app = InstaMon()
    app.main()
