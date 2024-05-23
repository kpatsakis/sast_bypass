# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-798_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 369 bytes
from django.http import HttpResponse
from django.shortcuts import redirect

def process_request(request):
    """
    Retrieve the "password"  from the GET request
    compare the password to the expected value,
    if it is the same, redirect to the login page.
    """
    password = request.GET['password']
    if password == 'myPa55word':
        redirect('login')