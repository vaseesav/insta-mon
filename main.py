"""
    Python script for tracking and recording activity of a single Instagram account.

    /*Changes
    * Made the script new from scratch.
    */

    V0.10 <--> 17.04.2023
"""

import instaloader
import sqlite3


class InstaMon:
    def __init__(self):
        self.settings_input = SettingsInput()

    def main(self):
        """
        Function that executes the modules of the script.
        :return: None
        """
        target_username = self.settings_input.enter_target_username()
        user_login_details = self.settings_input.enter_login_details()

        connect = sqlite3.connect(target_username + "-data.db")
        cursor = connect.cursor()

        instagram_scraper = InstagramScraper(target_username, user_login_details)
        db_creator = DbCreator(cursor, target_username)

        meta_data = instagram_scraper.get_metadata()
        profile_picture_url = instagram_scraper.get_profile_picture_url()
        profile_posts = instagram_scraper.get_posts()

        data_sorter = DataSorter(meta_data, profile_posts)

        meta_data_sorted = data_sorter.get_metadata()
        profile_posts_sorted = data_sorter.get_posts()

        db_inserter = DbInserter(meta_data_sorted, profile_picture_url, profile_posts_sorted)

        db_creator.create_db()
        db_inserter.insert_db()


class SettingsInput:
    @staticmethod
    def enter_target_username():
        target_username = input("Enter target username: ")
        return target_username

    @staticmethod
    def enter_login_details():
        login_details = input("Enter login details: ")
        return login_details


class InstagramScraper:
    def __init__(self, target, user):
        self.target = target
        self.user = user
        self.bot = instaloader.Instaloader()
        self.profile = instaloader.Profile.from_username(self.bot.context, self.target)

    def get_metadata(self):
        """
        Function that scraps the metadata of a user.
        :return: profile_metadata
        """
        try:
            profile_metadata = self.profile
            return profile_metadata
        except Exception as e:
            print("Something went wrong during the metadata request.", e)

    def get_profile_picture_url(self):
        """
        Function that scraps the profile picture url of a user.
        :return: profile_picture
        """
        try:
            profile_picture = self.profile.get_profile_pic_url()
            return profile_picture
        except Exception as e:
            print("Something went wrong during the profile picture url request.", e)

    def get_posts(self):
        """
        Function that scraps the posts of a user including all post data.
        :return: posts
        """
        try:
            if not self.profile.is_private:
                posts = self.profile.get_posts()
                return posts
        except Exception as e:
            print("Something went wrong during the get post request.", e)


class DataSorter:
    def __init__(self, meta_data, profile_posts):
        self.meta_data = meta_data
        self.profile_posts = profile_posts

    def get_metadata(self):
        pass

    def get_posts(self):
        pass


class DbCreator:
    def __init__(self, cursor, target_username):
        self.cursor = cursor
        self.target_username = target_username

    def table_exists(self):
        """
        Function that checks if all the tables are existing.
        :return: Boolean
        """
        cursor = self.cursor
        table_list = ["target", "posts"]
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"

        try:
            for table_name in table_list:
                cursor.execute(query, (table_name,))
                if cursor.fetchone() is not None:
                    return True
        except sqlite3.Error as se:
            print("Something went wrong fetching tables.", se)
        except Exception as e:
            print("Something went wrong during the existence check of a table.", e)

    def create_target_table(self):
        """
        Function that creates a target table.
        :return: None
        """
        cursor = self.cursor

        try:
            cursor.execute('''
            CREATE TABLE target (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_id TEXT KEY,
                name TEXT NOT NULL,
                username TEXT NOT NULL,
                bio TEXT,
                post_counter INTEGER,
                follower INTEGER,
                followings INTEGER,
                profile_picture_path TEXT,
                profile BLOB, 
                unix_timestamp INTEGER NOT NULL
            );
            ''')
        except sqlite3.Error as se:
            print("Something went wrong creating a table.", se)
        except Exception as e:
            print("Something went wrong creating a table.", e)

    def create_posts_table(self):
        """
        Function that creates a posts table.
        :return: None
        """
        cursor = self.cursor

        try:
            cursor.execute('''
            CREATE TABLE posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                caption TEXT,
                location TEXT,
                like_amount INTEGER,
                likes TEXT,
                comment_amount INTEGER,
                comments TEXT,
                image_path TEXT,
                image BLOB, 
                post_id INTEGER,
                unix_post_date INTEGER,
                unix_timestamp INTEGER NOT NULL
            );
            ''')
        except sqlite3.Error as se:
            print("Something went wrong creating a table.", se)
        except Exception as e:
            print("Something went wrong creating a table.", e)

    def create_db(self):
        """
        Function that creates the predefined databases.
        :return: None
        """
        try:
            if not self.table_exists():
                self.create_target_table()
                self.create_posts_table()
        except sqlite3.Error as se:
            print("Something went wrong creating the tables.", se)
        except Exception as e:
            print("Something went wrong creating the tables.", e)


class DbInserter:
    def __int__(self, meta_data_sorted, profile_picture_url, profile_posts_sorted):
        self.meta_data_sorted = meta_data_sorted
        self.profile_picture_picture_url = profile_picture_url
        self.profile_posts_sorted = profile_posts_sorted


if __name__ == "__main__":
    app = InstaMon()
    app.main()
