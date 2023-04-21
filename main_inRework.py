"""
    Python script for tracking and recording activity of a single Instagram account.

    /*Changes
    * Made the script new from scratch.
    */

    V0.10 <--> 17.04.2023
"""
from datetime import datetime
from pathlib import Path

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

        table_list = ["target", "posts"]
        db_creator = DbCreator(connect, cursor, target_username, table_list)
        db_creator.create_db()

        instagram_scraper = InstagramScraper(target_username, user_login_details)
        meta_data = instagram_scraper.get_metadata()
        profile_posts = instagram_scraper.get_posts()
        instagram_scraper.get_profile_picture()

        data_sorter = DataSorter(meta_data, profile_posts)
        meta_data_sorted = data_sorter.get_metadata()

        db_inserter = DbInserter(connect, cursor, meta_data_sorted)
        db_inserter.insert_target_table()


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
            quit(-1)

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
            quit(-1)

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
            quit(-1)

    def get_profile_picture(self):
        """
        Function that downloads the profile picture.
        :return: None
        """
        try:
            profile = self.profile
            picture_url = self.get_profile_picture_url()
            path = Path(self.target.lower() + '/profile_picture')
            self.bot.download_title_pic(picture_url, path, 'profile_pic', profile)
        except Exception as e:
            print("Something went wrong during the profile picture download request.", e)


class DataSorter:
    def __init__(self, meta_data, profile_posts):
        self.meta_data = meta_data
        self.profile_posts = profile_posts

    def get_metadata(self):
        """
        Function that gets the metadata and sorts it so that it can be inserted into the database.
        :return: meta_data_sorted
        """
        try:
            name = self.meta_data.full_name
            username = self.meta_data.username
            bio = self.meta_data.biography
            is_private = self.meta_data.is_private
            post_amount = self.profile_posts.count
            follower = self.meta_data.followers
            followings = self.meta_data.followees
            meta_data_sorted = [name, username, bio, is_private, post_amount, follower, followings]

            return meta_data_sorted
        except Exception as e:
            print("Something went wrong filtering the metadata.", e)
            quit(-1)

    def get_posts(self):
        """
        Function that gets the posts and sorts the data so that it can be inserted into the database.
        TODO: Filter data, add function to get new posts
        :return: profile_posts_sorted
        """
        # caption
        # location
        # like_amount
        # likes
        # comment_amount
        # comments
        # image
        # unix_post_date
        return None


class DbCreator:
    def __init__(self, connect, cursor, target_username, table_list):
        self.connect = connect
        self.cursor = cursor
        self.target_username = target_username
        self.table_list = table_list

    def table_exists(self):
        """
        Function that checks if all the tables are existing.
        :return: Boolean
        """
        cursor = self.cursor
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"

        try:
            for table_name in self.table_list:
                cursor.execute(query, (table_name,))
                if cursor.fetchone() is not None:
                    return True
        except sqlite3.Error as se:
            print("Something went wrong fetching tables.", se)
            quit(-1)
        except Exception as e:
            print("Something went wrong during the existence check of a table.", e)
            quit(-1)

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
                name TEXT NOT NULL,
                username TEXT NOT NULL,
                bio TEXT,
                is_private INTEGER,
                post_amount INTEGER,
                follower INTEGER,
                followings INTEGER,
                unix_time INTEGER NOT NULL
            );
            ''')
        except sqlite3.Error as se:
            print("Something went wrong creating a table.", se)
            quit(-1)
        except Exception as e:
            print("Something went wrong creating a table.", e)
            quit(-1)

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
                unix_time INTEGER NOT NULL
            );
            ''')
        except sqlite3.Error as se:
            print("Something went wrong creating a table.", se)
            quit(-1)
        except Exception as e:
            print("Something went wrong creating a table.", e)
            quit(-1)

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
            quit(-1)
        except Exception as e:
            print("Something went wrong creating the tables.", e)
            quit(-1)
        finally:
            self.connect.commit()


class DbInserter:
    def __init__(self, connect, cursor, meta_data_sorted):
        self.connect = connect
        self.cursor = cursor
        self.meta_data_sorted = meta_data_sorted

    def insert_target_table(self):
        """
        Function that inserts the sorted data into the target table.
        :return: None
        """
        meta_data = self.meta_data_sorted
        unix_timestamp = datetime.now().timestamp()
        meta_data.extend([unix_timestamp])

        try:
            self.cursor.execute('''
            INSERT INTO target (name, username, bio, is_private, post_amount, follower, 'followings', unix_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', meta_data)

        except sqlite3.Error as se:
            print("Something went wrong inserting data into the target table.", se)
            quit(-1)
        except Exception as e:
            print("Something went wrong inserting data into the target table.", e)
            quit(-1)
        finally:
            self.connect.commit()
            self.connect.close()


if __name__ == "__main__":
    app = InstaMon()
    app.main()
