# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-502_mitre_1.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 543 bytes
import _pickle as cPickle, base64

def confirmAuth--- This code section failed: ---

 L.  10         0  SETUP_FINALLY        62  'to 62'

 L.  11         2  LOAD_GLOBAL              cPickle
                4  LOAD_METHOD              loads
                6  LOAD_GLOBAL              base64
                8  LOAD_METHOD              b64decode
               10  LOAD_FAST                'headers'
               12  LOAD_STR                 'AuthToken'
               14  BINARY_SUBSCR    
               16  CALL_METHOD_1         1  ''
               18  CALL_METHOD_1         1  ''
               20  STORE_FAST               'token'

 L.  12        22  LOAD_GLOBAL              check_hmac
               24  LOAD_FAST                'token'
               26  LOAD_STR                 'signature'
               28  BINARY_SUBSCR    
               30  LOAD_FAST                'token'
               32  LOAD_STR                 'data'
               34  BINARY_SUBSCR    
               36  LOAD_GLOBAL              getSecretKey
               38  CALL_FUNCTION_0       0  ''
               40  CALL_FUNCTION_3       3  ''
               42  POP_JUMP_IF_TRUE     48  'to 48'

 L.  13        44  LOAD_GLOBAL              AuthFail
               46  RAISE_VARARGS_1       1  'exception instance'
             48_0  COME_FROM            42  '42'

 L.  14        48  LOAD_FAST                'token'
               50  LOAD_STR                 'data'
               52  BINARY_SUBSCR    
               54  STORE_FAST               'secure_data'

 L.  15        56  LOAD_FAST                'secure_data'
               58  POP_BLOCK        
               60  RETURN_VALUE     
             62_0  COME_FROM_FINALLY     0  '0'

 L.  16        62  POP_TOP          
               64  POP_TOP          
               66  POP_TOP          

 L.  17        68  LOAD_GLOBAL              AuthFail
               70  RAISE_VARARGS_1       1  'exception instance'
               72  POP_EXCEPT       
               74  JUMP_FORWARD         78  'to 78'
               76  END_FINALLY      
             78_0  COME_FROM            74  '74'

Parse error at or near `RAISE_VARARGS_1' instruction at offset 70