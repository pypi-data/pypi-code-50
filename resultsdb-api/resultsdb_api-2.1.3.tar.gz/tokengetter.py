from __future__ import print_function

from openidc_client import OpenIDCClient
import sys

c = OpenIDCClient(app_identifier='resultsdb',
                  id_provider='https://iddev.fedorainfracloud.org/openidc/',
                  id_provider_mapping={'Token': 'Token',
                                       'Authorization': 'Authorization'},
                  client_id='python-fedora',
                  client_secret='notsecret')

# IDEALLY, the below code should work... but I messed up
# c = OpenIDCBaseClient('resultsdb', 'https://iddev.fedorainfracloud.org/',
#                        'python-fedora')
token = c.get_token(['https://pagure.io/taskotron/resultsdb/access'])

renew = False
try:
    if sys.argv[1] == 'renew':
        print("Renewing token...")
        renew = True
except IndexError:
    pass

if renew:
    newtoken = c.report_token_issue()
    if not newtoken:
        print("Seems like the current token is fine!")
    else:
        token = newtoken

print("Your token is:", token)
