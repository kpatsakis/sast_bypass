# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-703_author_2.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 289 bytes


def convert_to_int--- This code section failed: ---

 L.   6         0  SETUP_FINALLY        20  'to 20'

 L.   7         2  LOAD_GLOBAL              input
                4  LOAD_STR                 'Enter a number: '
                6  CALL_FUNCTION_1       1  ''
                8  STORE_FAST               'user_input'

 L.   8        10  LOAD_GLOBAL              int
               12  LOAD_FAST                'user_input'
               14  CALL_FUNCTION_1       1  ''
               16  POP_BLOCK        
               18  RETURN_VALUE     
             20_0  COME_FROM_FINALLY     0  '0'

 L.   9        20  DUP_TOP          
               22  LOAD_GLOBAL              ValueError
               24  COMPARE_OP               exception-match
               26  POP_JUMP_IF_FALSE    42  'to 42'
               28  POP_TOP          
               30  POP_TOP          
               32  POP_TOP          

 L.  10        34  POP_EXCEPT       
               36  JUMP_BACK             0  'to 0'
               38  POP_EXCEPT       
               40  JUMP_BACK             0  'to 0'
             42_0  COME_FROM            26  '26'
               42  END_FINALLY      
               44  JUMP_BACK             0  'to 0'

Parse error at or near `JUMP_BACK' instruction at offset 36