# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-601_sonar_4.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 333 bytes
from django.http import HttpResponseRedirect, HttpResponse

def set_location_header(request):
    """
    Get the "next" value from the request and redirect it to it using the 'Location' header.
    """
    url = request.GET.get('next', '/')
    response = HttpResponse(status=302)
    response['Location'] = url
    return response