# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-117_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 441 bytes
import logging

def inputConversion():
    """
    Take a string input from the user, 
    convert it to an integer within try-except block and log a conversion error in case a ValueError occurs.
    Return the converted user input.
    """
    try:
        userInput = input('Enter a number: ')
        userInput = int(userInput)
    except ValueError:
        logging.error('The input was not a number: ' + userInput)
    else:
        return userInput