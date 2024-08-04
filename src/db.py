"""Database module of insta-mon. Containing the database logic."""

import logging
import sqlite3
import threading
import time
from typing import Optional

import src
from src.config import config
from src.data_models import User
from src.data_models.post.imagepost import ImagePost
from src.data_models.post.reelpost import ReelPost
from src.data_models.post.storypost import StoryPost
from src.log import setup_logging

_db_connection = None
_db_connections = None

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


def db_connection() -> sqlite3:
    """Internal helper function to create database at its first use

    Returns:
        sqlite3.Connection: Singleton database instance, thread safe
    """
    global _db_connection, _db_connections
    if _db_connections is None:
        _db_connections = dict()

    curr_thread_id = threading.current_thread()
    if curr_thread_id in _db_connections:
        return _db_connections[threading.current_thread()]

    _db_connection = sqlite3.connect(config.get('DB_SQ3_FILE'), isolation_level=None,
                                     check_same_thread=False)
    _db_connection.row_factory = sqlite3.Row
    _db_connection.execute('PRAGMA foreign_keys = ON;')
    _db_connection.execute('''
        CREATE TABLE IF NOT EXISTS "Config" (
            "Key"	TEXT NOT NULL UNIQUE PRIMARY KEY,
            "Value"	TEXT
        );
    ''')

    _db_connection.execute('''
        CREATE TABLE IF NOT EXISTS "User" (
            "Id" INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
            "UserId"  TEXT,
            "Username"  TEXT,
            "Name"  TEXT,
            "Biography" TEXT,
            "PostAmount" INTEGER,
            "FollowerAmount" INTEGER,
            "FollowsAmount" INTEGER,
            "ProfileImagePath" TEXT,
            "TimeStamp" INTEGER
        );
    ''')

    _db_connection.execute('''
        CREATE TABLE IF NOT EXISTS "Post" (
            "Id" INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
            "PostId"  TEXT,
            "PostType" TEXT,
            "MediaPath" TEXT,
            "Description" Text,
            "LikeAmount"  INTEGER,
            "CommentAmount" INTEGER,
            "TimeStamp" INTEGER
        );
    ''')

    _db_connection.commit()
    _db_connections[curr_thread_id] = _db_connection
    return _db_connection


def insert_config(key: str, value: str) -> None:
    """
    Function that inserts the config table.

    :param key: Config key to insert.:
    :param value: Config value.:  .
    """
    db_connection().execute(
        """
        INSERT OR IGNORE INTO Config (Key, Value)
        VALUES (?, ?)
        """,
        (key,
         value)
    )
    db_connection().commit()


def insert_user(user: User) -> None:
    """
    Function that inserts the user table.

    :param user: User object to insert in the database.
    """
    db_connection().execute(
        """
        INSERT OR IGNORE INTO User (UserId, Username, Name, Biography, PostAmount, FollowerAmount,
         FollowsAmount, ProfileImagePath, TimeStamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (user.uid,
         user.username,
         user.name,
         user.bio,
         user.post_amount,
         user.follower_amount,
         user.follows_amount,
         user.profile_image_path,
         int(time.time()))
    )
    db_connection().commit()


def insert_post(post) -> None:
    """
    Insert a post into the Post table.

    :param post: An instance of ImagePost, ReelPost, or StoryPost.
    """
    current_time = int(time.time())

    if isinstance(post, ImagePost):
        db_connection().execute(
            """
            INSERT OR IGNORE INTO Post (PostId, PostType, MediaPath, Description,
             LikeAmount, CommentAmount, TimeStamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (*post.to_tuple(), current_time)
        )
    elif isinstance(post, ReelPost):
        db_connection().execute(
            """
           INSERT OR IGNORE INTO Post (PostId, PostType, MediaPath, Description,
            LikeAmount, CommentAmount, TimeStamp)
           VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (*post.to_tuple(), current_time)
        )
    elif isinstance(post, StoryPost):
        db_connection().execute(
            """
            INSERT OR IGNORE INTO Post (PostId, PostType, MediaPath, Description,
             LikeAmount, CommentAmount, TimeStamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (*post.to_tuple(), current_time)
        )
    else:
        raise ValueError("Unsupported post type")

    db_connection().commit()


def update_config(key: str, value: str) -> None:
    """
    Function that updates the config table.

    :param key: Config key to update.
    :param value: New config value.
    """
    db_connection().execute(
        """
        UPDATE Config
        SET Value = ?
        WHERE Key = ?
        """,
        (value, key)
    )
    db_connection().commit()


def update_user(user: User) -> None:
    """
    Function that updates the user table.

    :param user: User object to update in the database.
    """
    db_connection().execute(
        """
        UPDATE User
        SET Username = ?,
            Name = ?,
            Biography = ?,
            PostAmount = ?,
            FollowerAmount = ?,
            FollowsAmount = ?,
            ProfileImagePath = ?
        WHERE UserId = ?
        """,
        (user.username,
         user.name,
         user.bio,
         user.post_amount,
         user.follower_amount,
         user.follows_amount,
         user.profile_image_path,
         user.uid)
    )
    db_connection().commit()


def update_post(post) -> None:
    """
    Update a post in the Post table.

    :param post: An instance of ImagePost, ReelPost, or StoryPost.
    """
    if isinstance(post, ImagePost):
        db_connection().execute(
            """
            UPDATE Post
            SET PostType = ?,
                MediaPath = ?,
                Description = ?,
                LikeAmount = ?,
                CommentAmount = ?
            WHERE PostId = ?
            """, post.to_tuple() + (post.post_id,)
        )
    elif isinstance(post, ReelPost):
        db_connection().execute(
            """
            UPDATE Post
            SET PostType = ?,
                MediaPath = ?,
                Description = ?,
                LikeAmount = ?,
                CommentAmount = ?
            WHERE PostId = ?
            """, post.to_tuple() + (post.post_id,)
        )
    elif isinstance(post, StoryPost):
        db_connection().execute(
            """
            UPDATE Post
            SET PostType = ?,
                MediaPath = ?,
                Description = ?,
                LikeAmount = ?,
                CommentAmount = ?
            WHERE PostId = ?
            """, post.to_tuple() + (post.post_id,)
        )
    else:
        raise ValueError("Unsupported post type")

    db_connection().commit()


def get_last_user_info() -> Optional[User]:
    """
       Function that gets the latest user entry.
       """
    conn = db_connection()
    result = conn.execute(
        """
        SELECT *
        FROM User
        ORDER BY id DESC
        LIMIT 1;
        """
    )

    last_entry = result.fetchone()

    if last_entry:
        user = User(
            uid=last_entry[1],
            username=last_entry[2],
            name=last_entry[3],
            bio=last_entry[4],
            post_amount=last_entry[5],
            follower_amount=last_entry[6],
            follows_amount=last_entry[7],
            profile_image_path=last_entry[8]
        )
        return user

    return None


def get_last_post_info() -> Optional[object]:
    """
       Function that gets the latest post-entry.
       """
    conn = db_connection()
    result = conn.execute(
        """
        SELECT *
        FROM Post
        ORDER BY id DESC
        LIMIT 1;
        """
    )

    last_entry = result.fetchone()

    if last_entry:
        post = src.data_models.post.Post(
            post_id=last_entry[1],
            post_type=last_entry[2],
            media_path=last_entry[3],
            description=last_entry[4],
            like_amount=last_entry[5],
            comment_amount=last_entry[6],
        )
        return post

    return None
