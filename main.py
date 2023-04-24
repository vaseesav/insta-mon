from database.db_creator import DbCreator
from database.db_inserter import DbInserter
from input.data_input import DataInput
from instagram.instagram_scraper import InstagramScraper
from instagram.instagram_data_sorter import DataSorter


class InstaMon:
    def __init__(self):
        self.target_name = DataInput().get_target_username()
        self.db_name = self.target_name + "-data.db"
        self.db_creator = DbCreator(self.db_name)
        self.instagram_scraper = InstagramScraper(self.target_name)
        self.meta_data = self.instagram_scraper.get_metadata()
        self.user_posts_data = self.instagram_scraper.get_posts()
        self.data_sorter = DataSorter(self.meta_data, self.user_posts_data)
        self.meta_data_sorted = self.data_sorter.get_metadata()
        self.db_inserter = DbInserter(self.db_name, self.meta_data_sorted)

    def main(self):
        # Create database and its tables
        self.db_creator.create_tables()

        # Inserts the sorted data into the tables
        self.db_inserter.insert_target_table()


if __name__ == "__main__":
    app = InstaMon()
    app.main()
