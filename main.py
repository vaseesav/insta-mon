from database.db_creator import DbCreator


class InstaMon:
    def __init__(self):
        self.target_name =
        self.db_name = self.target_name + "-data.db"
        self.db_creator = DbCreator(self.db_name)

    def main(self):
        # Create database and its tables
        self.db_creator.create_tables()


if __name__ == "__main__":
    app = InstaMon()
    app.main()
