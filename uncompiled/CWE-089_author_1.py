# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-089_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 406 bytes
import mysql.connector

def get_connection():
    """
    Return a connection to the database
    """
    return mysql.connector.connect(host='localhost', user='', passwd='')


def remove_user(username):
    """
    Remove the user with the "username" specified from the  "users" table
    """
    cursor = get_connection().cursor()
    cursor.execute("DELETE FROM users WHERE username = '%s'" % username)