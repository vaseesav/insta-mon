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