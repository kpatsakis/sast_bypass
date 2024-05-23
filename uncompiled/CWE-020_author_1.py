# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-020_author_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 272 bytes
import yaml

def yaml_load--- This code section failed: ---

 L.   9         0  LOAD_GLOBAL              open
                2  LOAD_FAST                'filename'
                4  LOAD_STR                 'r'
                6  CALL_FUNCTION_2       2  ''
                8  SETUP_WITH           44  'to 44'
               10  STORE_FAST               'f'

 L.  10        12  LOAD_GLOBAL              yaml
               14  LOAD_ATTR                load
               16  LOAD_FAST                'f'
               18  LOAD_GLOBAL              yaml
               20  LOAD_ATTR                BaseLoader
               22  LOAD_CONST               ('Loader',)
               24  CALL_FUNCTION_KW_2     2  '2 total positional and keyword args'
               26  STORE_FAST               'data'

 L.  11        28  LOAD_FAST                'data'
               30  POP_BLOCK        
               32  ROT_TWO          
               34  BEGIN_FINALLY    
               36  WITH_CLEANUP_START
               38  WITH_CLEANUP_FINISH
               40  POP_FINALLY           0  ''
               42  RETURN_VALUE     
             44_0  COME_FROM_WITH        8  '8'
               44  WITH_CLEANUP_START
               46  WITH_CLEANUP_FINISH
               48  END_FINALLY      

Parse error at or near `ROT_TWO' instruction at offset 32