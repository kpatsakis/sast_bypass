# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-425_author_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 382 bytes
from django.http import HttpResponse

def getResource(request):
    """
    Get username and date from the request, then
    send the file to the user by creating path by the username and date.
    """
    username = request.GET.get('username')
    date = request.GET.get('date')
    path = './' + username + '/' + date
    return HttpResponse(open('./static/' + path, 'r').read())