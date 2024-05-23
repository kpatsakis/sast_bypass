# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-367_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 248 bytes
import os

def readFile--- This code section failed: ---

 L.  10         0  LOAD_GLOBAL              os
                2  LOAD_ATTR                path
                4  LOAD_METHOD              exists
                6  LOAD_FAST                'fileName'
                8  CALL_METHOD_1         1  ''
               10  POP_JUMP_IF_FALSE    50  'to 50'

 L.  11        12  LOAD_GLOBAL              open
               14  LOAD_FAST                'fileName'
               16  LOAD_STR                 'r'
               18  CALL_FUNCTION_2       2  ''
               20  SETUP_WITH           44  'to 44'
               22  STORE_FAST               'f'

 L.  12        24  LOAD_FAST                'f'
               26  LOAD_METHOD              read
               28  CALL_METHOD_0         0  ''
               30  POP_BLOCK        
               32  ROT_TWO          
               34  BEGIN_FINALLY    
               36  WITH_CLEANUP_START
               38  WITH_CLEANUP_FINISH
               40  POP_FINALLY           0  ''
               42  RETURN_VALUE     
             44_0  COME_FROM_WITH       20  '20'
               44  WITH_CLEANUP_START
               46  WITH_CLEANUP_FINISH
               48  END_FINALLY      
             50_0  COME_FROM            10  '10'

Parse error at or near `ROT_TWO' instruction at offset 32