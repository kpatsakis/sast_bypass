# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: original_files/CWE-090_codeql_1.py
# Compiled at: 2024-01-25 22:29:31
# Size of source mod 2**32: 663 bytes
from flask import request, Flask
import ldap
app = Flask(__name__)

@app.route('/normal')
def normal():
    """
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    """
    unsafe_dc = request.args['dc']
    unsafe_filter = request.args['username']
    dn = 'dc={}'.format(unsafe_dc)
    search_filter = '(user={})'.format(unsafe_filter)
    ldap_connection = ldap.initialize('ldap://127.0.0.1')
    user = ldap_connection.search_s(dn, ldap.SCOPE_SUBTREE, search_filter)
    return str(user)