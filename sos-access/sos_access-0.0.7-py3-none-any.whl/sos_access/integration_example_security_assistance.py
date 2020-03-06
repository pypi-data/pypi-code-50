from sos_access.client import SOSAccessClient
from sos_access.schemas import AlarmRequest

import logging
import datetime

logger = logging.getLogger()
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

logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

TRANSMITTER_CODE = '999666'
TRANSMITTER_TYPE = 'SIA'
AUTH = '000000000000000'

# TODO: Document. Transmitterarea can be used to iniitat a different workflow at the agent.

ADDRESS = ('195.198.14.14', 19000)

# client = SOSAccessClient(transmitter_code=TRANSMITTER_CODE,
#                         transmitter_type=TRANSMITTER_TYPE, authentication=AUTH,
#                         receiver_address=ADDRESS, receiver_id='SOSA',
#                         use_single_receiver=True)

client = SOSAccessClient(transmitter_code=TRANSMITTER_CODE,
                         transmitter_type=TRANSMITTER_TYPE, authentication=AUTH,
                         receiver_address=ADDRESS, receiver_id='',
                         secondary_receiver_address=ADDRESS)

result = client.send_alarm(event_code='AL', detector='1',
                           detector_text='detector', transmitter_area='1',
                           reference='test', section='1',
                           section_text='section',
                           additional_info={'Testing testing': 'cool',
                                            'testing 2 testing 2': 'awesome'})
# client.restore_alarm(event_code='AL')

# result = client.ping()
# Not the password then testing request new password. Otherwise youll get locked out!
# client.request_new_auth()

print(result)

# event_coder.
