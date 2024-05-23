# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-089_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 511 bytes
import mysql.connector

def get_connection():
    """
    Return a connection to the database
    """
    return mysql.connector.connect(host='localhost', user='', passwd='')


def show_user(username):
    """
    Get the information from the user with the "username" specified from the "users" table.
    Return the user information.
    """
    cursor = get_connection().cursor()
    cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
    user = cursor.fetchone()
    return user