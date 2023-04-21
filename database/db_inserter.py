import sqlite3
from datetime import datetime
from db_handler import DbHandler


class DbInserter:
    def __init__(self, db_name, meta_data_sorted):
        self.db_name = db_name
        self.db_handler = DbHandler(db_name)
        self.meta_data_sorted = meta_data_sorted

    def insert_table(self):
        """
        Function which runs the insertion into tables.
        """
        self.insert_target_table()
        self.insert_posts_table()
        self.db_handler.connection.commit()

    def insert_target_table(self):
        """
        Function that inserts the target data into the target table.
        """
        cursor = self.db_handler.cursor()
        meta_data = self.meta_data_sorted
        unix_timestamp = datetime.now().timestamp()
        meta_data.extend([unix_timestamp])

        try:
            cursor.execute('''
            INSERT INTO target (name, username, bio, is_private, post_amount, follower, 'followings', unix_time)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', meta_data)
        except sqlite3.Error as se:
            print("An error occurred while inserting data into target table.", se)
            quit(-1)
        except Exception as e:
            print("An error occurred while inserting data into target table.", e)
            quit(-1)

    def insert_posts_table(self):
        """
        Function that inserts the posts data into the target table.
        """
        pass
