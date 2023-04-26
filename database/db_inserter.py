import sqlite3
from datetime import datetime
from database.db_handler import DbHandler
from logger.logger_handler import LoggingHandler


class DbInserter:
    def __init__(self, db_name, meta_data_sorted, image_name):
        db_name = db_name
        self.db_handler = DbHandler(db_name)
        self.meta_data_sorted = meta_data_sorted
        self.image_name = image_name
        self.logger = LoggingHandler(self.__class__.__name__).logger

    def insert_table(self):
        """
        Function which runs the insertion into tables.
        """
        self.insert_target_table()
        self.insert_posts_table()

    def image_to_binary(self, filename):
        try:
            with open(filename, 'rb') as f:
                image_data = f.read()
                return image_data
        except Exception as e:
            print("An error occurred while converting the image to binary", e)
            self.logger.error('An error occurred while converting the image to binary', e)
            quit(-1)

    def insert_target_table(self):
        """
        Function that inserts the target data into the target table.
        """
        try:
            self.logger.info("Inserting data into target table.")
            cursor = self.db_handler.cursor
            meta_data = self.meta_data_sorted
            unix_timestamp = datetime.now().timestamp()
            image_data = self.image_to_binary(self.image_name)
            meta_data.extend([unix_timestamp])
            meta_data.extend([image_data])
            cursor.execute('''
            INSERT INTO target (name, username, bio, is_private, post_amount, follower, 'followings', unix_time, profile_picture)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', meta_data)
        except sqlite3.Error as se:
            print("An error occurred while inserting data into target table.", se)
            self.logger.error('An error occurred while inserting data into target table.', se)
            quit(-1)
        except Exception as e:
            print("An error occurred while inserting data into target table.", e)
            self.logger.error('An error occurred while inserting data into target table.', e)
            quit(-1)
        finally:
            self.db_handler.connection.commit()

    def insert_posts_table(self):
        """
        Function that inserts the posts data into the target table.
        """
        pass
