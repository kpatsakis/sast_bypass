# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-414_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 546 bytes
import threading, time

def getData(dataStart, dataLimit, thread):
    """
    Check if the dataStart is less than or equal to dataLimit.
    If so, acquire a thread lock, increase the dataStart by 1 by, and then unlock the thread.
    Print which thread is currently accessing the data
    """
    lock = threading.Lock()
    if dataStart <= dataLimit:
        lock.acquire()
        dataStart += 1
        lock.release()
    print('data from A :: ' + str(dataStart) + ' Accessor thread :: ' + threading.get_ident())
    time.sleep(0.5)