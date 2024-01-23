#! /usr/bin/env python3

"""
Insta-mon: A tool to monitor someone's Instagram account

This module contains the main entry point for the application.
"""

import sys

if __name__ == '__main__':
    # Check if the correct python version is being used
    python_version = sys.version.split()[0]

    if sys.version_info < (3, 5):
        print('The minimum required Python version is 3.5+ \n'
              'The version you are using is %s' % python_version)
        quit(-1)

    import instamon

    instamon.main()
