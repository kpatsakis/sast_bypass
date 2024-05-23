# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-200_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 712 bytes
import logging

def isAuthorizedUser(userId):
    pass


def getUserBankAccount--- This code section failed: ---

 L.  12         0  LOAD_GLOBAL              isAuthorizedUser
                2  LOAD_FAST                'userId'
                4  CALL_FUNCTION_1       1  ''
                6  POP_JUMP_IF_FALSE    94  'to 94'

 L.  13         8  SETUP_FINALLY        38  'to 38'

 L.  14        10  LOAD_STR                 "SELECT * FROM user_bank_account WHERE user_id = '"
               12  LOAD_FAST                'userId'
               14  BINARY_ADD       
               16  LOAD_STR                 "'"
               18  BINARY_ADD       
               20  STORE_FAST               'sql'

 L.  15        22  LOAD_FAST                'connection'
               24  LOAD_METHOD              execute
               26  LOAD_FAST                'sql'
               28  CALL_METHOD_1         1  ''
               30  STORE_FAST               'result'

 L.  16        32  LOAD_FAST                'result'
               34  POP_BLOCK        
               36  RETURN_VALUE     
             38_0  COME_FROM_FINALLY     8  '8'

 L.  17        38  DUP_TOP          
               40  LOAD_GLOBAL              Exception
               42  COMPARE_OP               exception-match
               44  POP_JUMP_IF_FALSE    90  'to 90'
               46  POP_TOP          
               48  STORE_FAST               'e'
               50  POP_TOP          
               52  SETUP_FINALLY        78  'to 78'

 L.  18        54  LOAD_GLOBAL              logging
               56  LOAD_METHOD              error
               58  LOAD_STR                 'Unable to retrieve account information from database. Query: '
               60  LOAD_FAST                'sql'
               62  FORMAT_VALUE          0  ''
               64  BUILD_STRING_2        2 
               66  CALL_METHOD_1         1  ''
               68  POP_TOP          

 L.  19        70  LOAD_FAST                'e'
               72  RAISE_VARARGS_1       1  'exception instance'
               74  POP_BLOCK        
               76  BEGIN_FINALLY    
             78_0  COME_FROM_FINALLY    52  '52'
               78  LOAD_CONST               None
               80  STORE_FAST               'e'
               82  DELETE_FAST              'e'
               84  END_FINALLY      
               86  POP_EXCEPT       
               88  JUMP_ABSOLUTE        98  'to 98'
             90_0  COME_FROM            44  '44'
               90  END_FINALLY      
               92  JUMP_FORWARD         98  'to 98'
             94_0  COME_FROM             6  '6'

 L.  21        94  LOAD_CONST               None
               96  RETURN_VALUE     
             98_0  COME_FROM            92  '92'

Parse error at or near `JUMP_ABSOLUTE' instruction at offset 88