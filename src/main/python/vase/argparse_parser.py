"""Insta-mon args module

This module handles the arguments parsed from the command line
"""

import argparse


class ArgParser:
    """
    Class which handles the available runtime arguments
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Instagram Login Parser")

        # Adds the username argument
        self.parser.add_argument(
            "-u",
            "--username",
            type=str,
            help="Instagram username",
            action="store",
            dest="username",
            default=None,
        )

        # Adds the password argument
        self.parser.add_argument(
            "-p",
            "--password",
            type=str,
            help="Instagram password",
            action="store",
            dest="password",
            default=None,
        )

        # Adds the verification_code argument
        self.parser.add_argument(
            "-v",
            "--verification_code",
            type=str,
            help="Instagram verification code",
            action="store",
            dest="verification_code",
            default=None,
        )

    def parse_args(self):
        args = self.parser.parse_args()

        # Validate input
        # if (password || username) --> password requires username || username requires password
        # if (verify_code) --> verify_code requires username && password

        if args.username is not None and args.password is None:
            raise ValueError("Username and password must be provided together")
        if args.verification_code is not None and (args.username is None or args.password is None):
            raise ValueError("Verification code can only be provided if username and password are also provided")

        return args
