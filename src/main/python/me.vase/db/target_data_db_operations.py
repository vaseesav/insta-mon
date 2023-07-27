import sqlite3


class TargetDatabase:
    """sqlite3 database class that manages the target database"""

    def __init__(self, location: str):
        self.location = location
        self.connection = None
        self.cursor = None

    def open_connection(self):
        """open sqlite3 connection"""
        self.connection = sqlite3.connect(self.location)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        """close sqlite3 connection"""
        self.connection.close()

    def table_exists(self, table):
        """
        Function that returns a boolean indicating whether the given table exists or not.
        :param table:
        :return: boolean
        """
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
        self.open_connection()

        try:
            self.cursor.execute(query, (table,))
            if self.cursor.fetchone() is not None:
                return True
        except sqlite3.Error as se:
            print("An error occurred while checking for tables.", se)
            quit(-1)
        except Exception as e:
            print("An error occurred while checking for tables.", e)
            quit(-1)
        finally:
            self.close_connection()


class CreateTargetDatabase:
    pass
