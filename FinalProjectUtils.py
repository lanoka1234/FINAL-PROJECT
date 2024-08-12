# Name: Laura Anoka
# Student ID: 2172987
#
# FinalProjectUtils.py
# This script contains utility functions that are used across different parts of the project.

import os

def check_and_create_directory(directory_name):
    """
    Checks if a directory exists, and creates it if it doesn't.
    
    :param directory_name: Name of the directory to check/create.
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

# Example usage:
check_and_create_directory('Output')
