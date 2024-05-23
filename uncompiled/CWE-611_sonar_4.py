# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-611_sonar_4.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 358 bytes
import xml.sax

def get_root():
    """
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    """
    parser = xml.sax.make_parser()
    myHandler = MyHandler()
    parser.setContentHandler(myHandler)
    parser.setFeature(feature_external_ges, True)
    parser.parse('resources/config.xml')
    return     return parser