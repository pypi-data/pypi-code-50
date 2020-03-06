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

TRANSMITTER_CODE = 'IK980102'
TRANSMITTER_TYPE = 'SV301'
AUTH = '000000000000000'

#ADDRESS = ('194.14.58.16', 19200)
ADDRESS = ('alarmtest1.sosalarm.se', 19100)


client = SOSAccessClient(transmitter_code=TRANSMITTER_CODE,
                         transmitter_type=TRANSMITTER_TYPE, authentication=AUTH,
                         receiver_address=ADDRESS, receiver_id='SOSA',
                         use_single_receiver=True, use_tls=True)

client.send_alarm(event_code='AL')
