import sqlite3

from db_handler import DbHandler


class DbCreator:
    def __init__(self, db_name):
        self.db_name = db_name
        self.db_handler = DbHandler(db_name)

    def create_tables(self):
        """
        Function which runs the creation of tables.
        """
        self.create_target_table()
        self.create_posts_table()
        self.db_handler.connection.commit()

    def table_exists(self, table_name):
        """
        Function which checks for the existence of a given table.
        :param table_name:
        :return: Boolean
        """
        cursor = self.db_handler.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"

        try:
            cursor.execute(query, (table_name,))
            if cursor.fetchone() is not None:
                return True
        except sqlite3.Error as se:
            print("An error occurred while checking for tables.", se)
            quit(-1)
        except Exception as e:
            print("An error occurred while checking for tables.", e)
            quit(-1)

    def create_target_table(self):
        """
        Function which creates the target table.
        """
        cursor = self.db_handler.cursor()

        try:
            if self.table_exists("target"):
                pass
            else:
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
            quit(-1)
        except Exception as e:
            print("An error occurred while creating the target table.", e)
            quit(-1)

    def create_posts_table(self):
        cursor = self.db_handler.cursor()

        try:
            if self.table_exists("posts"):
                pass
            else:
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
            quit(-1)
        except Exception as e:
            print("An error occurred while creating the posts table.", e)
            quit(-1)