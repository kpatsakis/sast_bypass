# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-477_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 185 bytes
import time

def currentTime():
    """
    Print the current processor time in seconds.
    """
    pro_time = time.clock()
    print('Current processor time (in seconds):', pro_time)