import argparse


class ArgParser:
    """Handles command-line arguments for Insta-mon."""

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(description="Insta-mon argument parser")
        self._add_arguments()
        self.args = self.parser.parse_args()

        # Store parsed arguments as instance attributes
        self.username: str = self.args.username
        self.password: str = self.args.password
        self.verification_code: str = self.args.verification_code

        self._validate_parsed_args()  # Validate after parsing

    def _add_arguments(self) -> None:
        """Adds optional arguments to the parser."""
        self.parser.add_argument(
            "-u",
            "--username",
            type=str,
            default=None,
            help="Insta username",
        )
        self.parser.add_argument(
            "-p",
            "--password",
            type=str,
            default=None,
            help="Insta password",
        )
        self.parser.add_argument(
            "-v",
            "--verification_code",
            type=str,
            default=None,
            help="Insta verification code (optional)",
        )

    def _validate_parsed_args(self) -> None:
        """Validates the parsed arguments."""
        if self.verification_code and not (self.username and self.password):
            raise ValueError("Verification code requires both username and password")
        if (self.username is None) ^ (self.password is None):  # Check for both or none
            raise ValueError("Username and password must be provided together")

    def get_username(self) -> str:
        """Returns the parsed username, or None if not provided."""
        return self.username

    def get_password(self) -> str:
        """Returns the parsed password, or None if not provided."""
        return self.password

    def get_verification_code(self) -> str:
        """Returns the parsed verification code, if provided."""
        return self.verification_code
