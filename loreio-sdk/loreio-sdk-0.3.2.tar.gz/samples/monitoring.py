import time

from loreiosdk.spyglass_script import Spyglass

url = 'wss://ui.getlore.io/storyteller'
user = 'USERNAME'
pwd = 'PWD'

spyglass = Spyglass(url, user, pwd)

(status, seqno, _) = spyglass.sync_cmd('session', ['payu_v3'])

tables = ['@blazenet_transactions']

for table in tables:
    (status, seqno, results) = spyglass.sync_cmd('aql', [
        ''' 'select count(*) from "{table}" where ingestion_date = \\'{date}\\'' '''
                                                 .format(table=table, date=time.strftime("%Y-%m-%d")), '--json'])
    assert results['data']['series'][0]['data'][0]['count'] > 0, "check failed for table : {} ".format(table)
