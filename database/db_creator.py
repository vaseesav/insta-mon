import sqlite3
from logger.logger_handler import LoggingHandler
from database.db_handler import DbHandler


class DbCreator:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_handler = DbHandler(db_name)
        self.logger = LoggingHandler(self.__class__.__name__).logger

    def create_tables(self):
        """
        Function which runs the creation of tables.
        """
        self.create_target_table()
        self.create_posts_table()

    def table_exists(self, table_name):
        """
        Function which checks for the existence of a given table.
        :param table_name:
        :return: Boolean
        """
        cursor = self.db_handler.cursor
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"

        try:
            cursor.execute(query, (table_name,))
            if cursor.fetchone() is not None:
                self.logger.info("Table {} exists.".format(table_name))
                return True
        except sqlite3.Error as se:
            print("An error occurred while checking for tables.", se)
            self.logger.warning('An error occurred while checking for tables.', se)
            quit(-1)
        except Exception as e:
            print("An error occurred while checking for tables.", e)
            self.logger.warning('An error occurred while checking for tables.', e)
            quit(-1)

    def create_target_table(self):
        """
        Function which creates the target table.
        """
        try:
            cursor = self.db_handler.cursor
            if self.table_exists("target"):
                pass
            else:
                self.logger.info("Creating target table.")
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
            print("An error occurred while creating the target table.", se)
            self.logger.critical('An error occurred while creating the target table.', se)
            quit(-1)
        except Exception as e:
            print("An error occurred while creating the target table.", e)
            self.logger.critical('An error occurred while creating the target table.', e)
            quit(-1)
        finally:
            self.db_handler.connection.commit()

    def create_posts_table(self):
        try:
            cursor = self.db_handler.cursor
            if self.table_exists("posts"):
                pass
            else:
                self.logger.info("Creating posts table.")
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
            print("An error occurred while creating the posts table.", se)
            self.logger.critical('An error occurred while creating the posts table.', se)
            quit(-1)
        except Exception as e:
            print("An error occurred while creating the posts table.", e)
            self.logger.critical('An error occurred while creating the posts table.', e)
            quit(-1)
        finally:
            self.db_handler.connection.commit()
