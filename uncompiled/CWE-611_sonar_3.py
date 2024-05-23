# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-611_sonar_3.py
# Compiled at: 2024-01-25 22:29:32
# Size of source mod 2**32: 443 bytes
from lxml import etree

def transform_xml():
    """
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    """
    parser = etree.XMLParser(resolve_entities=True)
    tree = etree.parse('resources/config.xml', parser)
    root_xsl = tree.getroot()
    ac = etree.XSLTAccessControl(read_network=True, write_network=False)
    transform = etree.XSLT(root_xsl, access_control=ac)
    return transform