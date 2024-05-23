# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-269_mitre_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 899 bytes
import os

def invalidUsername(username):
    pass


def raisePrivileges():
    pass


def lowerPrivileges():
    pass


def makeNewUserDir--- This code section failed: ---

 L.  23         0  LOAD_GLOBAL              invalidUsername
                2  LOAD_FAST                'username'
                4  CALL_FUNCTION_1       1  ''
                6  POP_JUMP_IF_FALSE    20  'to 20'

 L.  25         8  LOAD_GLOBAL              print
               10  LOAD_STR                 'Usernames cannot contain invalid characters'
               12  CALL_FUNCTION_1       1  ''
               14  POP_TOP          

 L.  26        16  LOAD_CONST               False
               18  RETURN_VALUE     
             20_0  COME_FROM             6  '6'

 L.  28        20  SETUP_FINALLY        52  'to 52'

 L.  29        22  LOAD_GLOBAL              raisePrivileges
               24  CALL_FUNCTION_0       0  ''
               26  POP_TOP          

 L.  30        28  LOAD_GLOBAL              os
               30  LOAD_METHOD              mkdir
               32  LOAD_STR                 '/home/'
               34  LOAD_FAST                'username'
               36  BINARY_ADD       
               38  CALL_METHOD_1         1  ''
               40  POP_TOP          

 L.  31        42  LOAD_GLOBAL              lowerPrivileges
               44  CALL_FUNCTION_0       0  ''
               46  POP_TOP          
               48  POP_BLOCK        
               50  JUMP_FORWARD         86  'to 86'
             52_0  COME_FROM_FINALLY    20  '20'

 L.  32        52  DUP_TOP          
               54  LOAD_GLOBAL              OSError
               56  COMPARE_OP               exception-match
               58  POP_JUMP_IF_FALSE    84  'to 84'
               60  POP_TOP          
               62  POP_TOP          
               64  POP_TOP          

 L.  33        66  LOAD_GLOBAL              print
               68  LOAD_STR                 'Unable to create new user directory for user:'
               70  LOAD_FAST                'username'
               72  BINARY_ADD       
               74  CALL_FUNCTION_1       1  ''
               76  POP_TOP          

 L.  34        78  POP_EXCEPT       
               80  LOAD_CONST               False
               82  RETURN_VALUE     
             84_0  COME_FROM            58  '58'
               84  END_FINALLY      
             86_0  COME_FROM            50  '50'

 L.  36        86  LOAD_CONST               True
               88  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_CONST' instruction at offset 80