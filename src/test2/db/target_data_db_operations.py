import sqlite3
from logger.log_controller import LogController


class DatabaseController:
    """sqlite3 database class that manages the target database"""

    def __init__(self, location: str):
        self.logger = LogController(self.__class__.__name__).logger
        self.location = location
        self.connection = None
        self.cursor = None

    def open_connection(self):
        """open sqlite3 connection"""
        self.connection = sqlite3.connect(self.location + ".db")
        self.cursor = self.connection.cursor()

    def close_connection(self):
        """close sqlite3 connection"""
        self.connection.close()

    def table_exists(self, table: str):
        """
        Function that returns a boolean indicating whether the given table exists or not.
        :param: table
        :return: boolean
        """
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        self.open_connection()

        try:
            self.logger.info("Checking if table exists.")
            self.cursor.execute(query, (table,))
            if self.cursor.fetchone() is not None:
                return True
        except sqlite3.Error as se:
            print("An error occurred while checking for tables.", se)
            self.logger.error("An error occurred while checking for tables.")
            quit(-1)
        except Exception as e:
            print("An error occurred while checking for tables.", e)
            self.logger.error("An error occurred while checking for tables.")
            quit(-1)
        finally:
            self.close_connection()


class CreateTargetDatabase:
    """sqlite3 database class that creates the tables"""

    def __init__(self, location: str):
        self.logger = LogController(self.__class__.__name__).logger
        self.database_controller = DatabaseController(location)

    def create_tables(self):
        self.create_target_table()
        self.create_posts_table()

    def create_target_table(self):
        """Function that creates the target table with the given items if it not already exists."""
        try:
            if self.database_controller.table_exists("target"):
                self.logger.info("The target table already exists.")
                pass
            else:
                self.logger.info("Creating the target table.")
                self.database_controller.open_connection()
                self.database_controller.cursor.execute('''
                CREATE TABLE target (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    username TEXT NOT NULL,
                    bio TEXT,
                    is_private INTEGER,
                    post_amount INTEGER,
                    follower INTEGER,
                    followings INTEGER,
                    profile_picture BLOB,
                    profile_picture_path TEXT,
                    unix_time INTEGER NOT NULL
                );
                ''')
        except sqlite3.Error as se:
            print("An error occurred while creating the target table.", se)
            self.logger.error("An error occurred while creating the target table.")
            quit(-1)
        except Exception as e:
            print("An error occurred while creating the target table.", e)
            self.logger.error("An error occurred while creating the target table.")
            quit(-1)
        finally:
            self.database_controller.connection.commit()
            self.database_controller.close_connection()

    def create_posts_table(self):
        """Function that creates the posts table with the given items if it not already exists."""
        try:
            if self.database_controller.table_exists("posts"):
                self.logger.info("The posts table already exists.")
                pass
            else:
                self.logger.info("Creating the posts table.")
                self.database_controller.open_connection()
                self.database_controller.cursor.execute('''
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
            self.logger.error("An error occurred while creating the posts table.")
            quit(-1)
        except Exception as e:
            print("An error occurred while creating the posts table.", e)
            self.logger.error("An error occurred while creating the posts table.")
            quit(-1)
        finally:
            self.database_controller.connection.commit()
            self.database_controller.close_connection()
