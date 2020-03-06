from sos_access.client import SOSAccessClient
from sos_access.schemas import AlarmRequest

"""
Krypterad:

Transmittercode: IK980102

Transmittertype: SV301

Authentication: 000000000000000

 

Okrypterad:

Transmittercode: IO980102

Transmittertype: SV300

Authentication: 000000000000000

 

Anslutningsuppgifter:

IP: 194.14.58.16/194.14.60.16

Krypterad port: 19100

Okrypterad port: 19000
"""

TRANSMITTER_CODE = 'IO980102'
TRANSMITTER_TYPE = 'SV300'
AUTH = '*Tlz!3dLWSQuYsv'

# TODO: Document. Transmitterarea can be used to iniitat a different workflow at the agent.

ADDRESS = ('194.14.58.16', 19000)

# client = SOSAccessClient(transmitter_code=TRANSMITTER_CODE,
#                         transmitter_type=TRANSMITTER_TYPE, authentication=AUTH,
#                         receiver_address=ADDRESS, receiver_id='SOSA',
#                         use_single_receiver=True)

client = SOSAccessClient(transmitter_code=TRANSMITTER_CODE,
                         transmitter_type=TRANSMITTER_TYPE, authentication=AUTH,
                         receiver_address=ADDRESS, receiver_id='SOSA',
                         secondary_receiver_address=('194.14.58.16', 19000))

#client.send_alarm(event_code='AL', additional_info={'Testing testing': 'cool',
#                                                    'testing 2 testing 2': 'awesome'})
# client.restore_alarm(event_code='AL')

result = client.ping()
# Not the password then testing request new password. Otherwise youll get locked out!
# client.request_new_auth()

print(result)
