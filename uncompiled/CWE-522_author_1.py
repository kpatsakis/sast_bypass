# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-522_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 492 bytes
import base64, MySQLdb

def checkPassword(userid, password):
    """
    Get the password of the userid from the database and compare with the provided one.
    """
    db = MySQLdb.connect(host='localhost', user='root', passwd='', db='test')
    cursor = db.cursor()
    cursor.execute('SELECT password FROM users WHERE userid = %s', (userid,))
    result = cursor.fetchone()
    if result is None:
        return False
    return base64.b64decode(result[0]) == password