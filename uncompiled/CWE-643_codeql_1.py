# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-643_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 490 bytes
from lxml import etree
from io import StringIO
from django.http import HttpResponse

def xpath_query(request):
    """
    Get the `xpath` value from the GET request,
    get the 'xml' value from the GET request,
    construct and parse the xml payload,
    return the result of the XPath query "/tag[@id={}]" format from the parsed xml
    """
    value = request.GET['xpath']
    f = StringIO(request.GET['xml'])
    tree = etree.parse(f)
    return tree.xpath("/tag[@id='%s']" % value)