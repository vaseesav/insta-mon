# Construction work in progress!
# Not fully working as of now!


# insta-mon
Python script for tracking and recording activity of a single Instagram account. 
Gathers user data, posts and timestamps and writes them into a database.


## Features

- Instagram monitoring
    - profiles (posts, stories, userdata)
- SQLite Database
    - Tables: User, Post, Config
- User login
    - email
    - password
    - 2FA

## Usage
To run the script, you will have to parse the target username as an argument. 
- "python3 main.py -u <email> -p <password> -t <target_username>"

You can also log into 2FA accounts:
- "python3 main.py [...] -f <code>"

## Authors

- [@vase](https://github.com/vaseesav)


## Please Note

Please note that this script is for theoretical purposes only and should not be used in real-world applications. If you choose to use this script, it is your responsibility to ensure that it complies with Instagram's terms of service. We recommend reviewing these terms before using this script or any other tools related to Instagram.


## Libraries

- [instagrapi](https://github.com/subzeroid/instagrapi) 


## [Milestones](https://github.com/vaseesav/insta-mon/milestones)


## Soon
- Stories
- working with multiple posts
- working with pinned posts
- session_id login
- use of user_id instead of target_username
