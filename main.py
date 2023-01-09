"""
    Python script to continuously monitor ones Instagram account.
    Saves data inside sqlite table.
    Early access version -- only handles main functionality.
    V0.09 <--> 09.01.2023
"""

import os
import uuid
import json
import sqlite3
from datetime import datetime
from instagramy import InstagramUser
from instagramy.plugins.download import *
from instagramy.core.cache import clear_caches

# String containing the path of the user session id file
login_file_path = "user_data.json"


def logged_in():
    """
    Checks if the user is logged into the IG Account.

    :param: json_object
    :exception: KeyError, Exception
    :return: boolean value of the logged in state
    """

    try:
        if os.path.isfile(login_file_path):
            with open(login_file_path, "r") as f:
                json_object = json.load(f)
                id = json_object['loginId']
                username = json_object['loginName']

                if not id or not username:
                    return False

            return True

    except KeyError as ke:
        print("Can't find the loginId or loginName in the user_data file.", ke)
    except Exception as ee:
        print("An error occurred searching the user_data file.", ee)


def load_user_login():
    """
    Loads the login details from the user_data.json.

    :param: json_object, json_node_loginId, json_node_loginName
    :exception: KeyError, Exception
    :return:list: username, id
    """

    try:
        with open(login_file_path, "r") as f:
            json_object = json.load(f)
            json_node_loginId = json_object['loginId']
            json_node_loginName = json_object['loginName']

        return {"account_name": json_node_loginName, "account_id": json_node_loginId}

    except KeyError as ke:
        print('loginId or loginName node was not found in file.', ke)
    except Exception as ee:
        print('An error occurred trying to load data from user_data file..', ee)


def register_user():
    """
    TODO: fix multiple usage of open
    Function initiating the registration process (Adding the username and the user id to the user_data.json).

    :param:id, username, json_object, login_id_node, login_name_node
    :return: username, id
    """

    try:
        # Variable that stores the IG Account id to log into
        id = input("Enter the session id of the user you are logging into! ") or "38566737751%3Ah7JpgePGAoLxJe%334"
        # Variable that stores the username of the user logged into
        username = input("Enter the username of the account you are willing to log into: ") or "none "

        with open(login_file_path, "w") as f:
            f.write('{ \n''"loginId": [], \n''"loginName": [] \n''}')

        with open(login_file_path, "r") as f:
            json_object = json.load(f)
            login_id_node = json_object['loginId']
            login_name_node = json_object['loginName']
            login_id_node.append(id)
            login_name_node.append(username)

        with open(login_file_path, "w") as f:
            json.dump(json_object, f)

    except Exception as ee:
        print("Something went wrong during the registration process.", ee)
        quit(-1)


def instagram_login():
    """
    Runs the login or register function and stores the login details.

    :param: user_data, username, id
    :return: user_data (username, id)
    """

    if logged_in():
        user_data = load_user_login()
        username = user_data["account_name"][0]
        id = user_data["account_id"][0]

        print("Welcome to InstaGod! Your are running the script as {username} with id {id} !".format(username=username,
                                                                                                     id=id))

        return user_data

    elif not logged_in():
        register_user()


def select_target():
    """
    Function to select the target.

    :param: target_username
    :return: target_username
    """
    try:
        target_username = input("Please enter Target's Instagram username: ")

        if target_username.isascii():
            return target_username

    except Exception as ee:
        print("An error occurred during the target declaration process.", ee)
        quit(-1)


def parse_target_information(target_username, id):
    """
    Gets the targets information from the Instagram API.

    :param: target_username, target_information, id
    :return: target_information
    """

    try:
        target = InstagramUser(target_username, from_cache=False, sessionid=id)
        target_information = {'all': target.user_data, 'name': target.fullname, 'pictures': target.posts_display_urls}
    except Exception as ee:
        print("Something went wrong during the parsing process.", ee)
        quit(-1)

    return target_information


def db_connect():
    """
    Initiates the connection to the db.

    :param: connect
    :return: connect
    """

    try:
        connect = sqlite3.connect(target_username + "-data.db")
        cursor = connect.cursor()

        return cursor

    except sqlite3.Error as se:
        print("Failed to connect to database.", se)
        quit(-1)


def db_create_target_data_table(cursor):
    """
    Creates the db table that stores basic target information.
    :param cursor:
    :return: Null
    """

    try:
        cursor.execute('''
        CREATE TABLE target (
            id INTEGER AUTOINCREMENT,
            target_id TEXT KEY,
            name TEXT NOT NULL,
            username TEXT NOT NULL,
            bio TEXT,
            post_counter INTEGER,
            follower INTEGER,
            following INTEGER, 
            unix_timestamp INTEGER NOT NULL
        );
        ''')

    except sqlite3.Error as se:
        print("Failed to create database.", se)


def db_create_posts_table(cursor):
    try:
        cursor.execute('''
        CREATE TABLE posts (
            id INTEGER AUTOINCREMENT,
            images BLOB,  
            likes INTEGER,
            comments INTEGER,
            deleted BIT NOT NULL,
            unix_delete TEXT,
            unix_timestamp INTEGER NOT NULL    
            );
            ''')

    except sqlite3.Error as se:
        print("Failed to create database.", se)


def db_create_follower_table(cursor):
    try:
        cursor.execute('''
        CREATE TABLE follower (
            id INTEGER AUTOINCREMENT,
            username TEXT,
            deleted BIT NOT NULL,
            unix_delete TEXT,
            unix_timestamp INTEGER NOT NULL    
            );
            ''')

    except sqlite3.Error as se:
        print("Failed to create database.", se)


def db_create_following_table(cursor):
    try:
        cursor.execute('''
        CREATE TABLE following (
            id INTEGER AUTOINCREMENT,
            username TEXT,
            deleted BIT NOT NULL,
            unix_delete TEXT,
            unix_timestamp INTEGER NOT NULL    
            );
            ''')

    except sqlite3.Error as se:
        print("Failed to create database.", se)


def db_create_stories_table(cursor):
    try:
        cursor.execute('''
        CREATE TABLE stories (
            id INTEGER AUTOINCREMENT,
            images BLOB,  
            deleted BIT NOT NULL,
            unix_delete TEXT,
            unix_timestamp INTEGER NOT NULL    
            );
            ''')

    except sqlite3.Error as se:
        print("Failed to create database.", se)


def db_handler():
    try:
        cursor = db_connect()

        db_create_target_data_table(cursor)

    except sqlite3.Error as se:
        print("Something went wrong during db processes.", se)
        quit(-1)
    except Exception as ee:
        print("Something went wrong during db processes.", ee)
        quit(-1)


# TODO: main function
instagram_login()

target_username = select_target()
id = load_user_login()["account_id"]

parse_target_information(target_username, id)
db_handler()
