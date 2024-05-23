# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-250_mitre_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 648 bytes
import os

def raisePrivileges():
    pass


def lowerPrivileges():
    pass


def makeNewUserDir--- This code section failed: ---

 L.  18         0  SETUP_FINALLY        32  'to 32'

 L.  19         2  LOAD_GLOBAL              raisePrivileges
                4  CALL_FUNCTION_0       0  ''
                6  POP_TOP          

 L.  20         8  LOAD_GLOBAL              os
               10  LOAD_METHOD              mkdir
               12  LOAD_STR                 '/home/'
               14  LOAD_FAST                'username'
               16  BINARY_ADD       
               18  CALL_METHOD_1         1  ''
               20  POP_TOP          

 L.  21        22  LOAD_GLOBAL              lowerPrivileges
               24  CALL_FUNCTION_0       0  ''
               26  POP_TOP          
               28  POP_BLOCK        
               30  JUMP_FORWARD         66  'to 66'
             32_0  COME_FROM_FINALLY     0  '0'

 L.  22        32  DUP_TOP          
               34  LOAD_GLOBAL              OSError
               36  COMPARE_OP               exception-match
               38  POP_JUMP_IF_FALSE    64  'to 64'
               40  POP_TOP          
               42  POP_TOP          
               44  POP_TOP          

 L.  23        46  LOAD_GLOBAL              print
               48  LOAD_STR                 'Unable to create new user directory for user:'
               50  LOAD_FAST                'username'
               52  BINARY_ADD       
               54  CALL_FUNCTION_1       1  ''
               56  POP_TOP          

 L.  24        58  POP_EXCEPT       
               60  LOAD_CONST               False
               62  RETURN_VALUE     
             64_0  COME_FROM            38  '38'
               64  END_FINALLY      
             66_0  COME_FROM            30  '30'

 L.  25        66  LOAD_CONST               True
               68  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `LOAD_CONST' instruction at offset 60