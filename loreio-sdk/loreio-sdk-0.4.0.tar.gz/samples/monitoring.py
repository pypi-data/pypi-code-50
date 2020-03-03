import time

from loreiosdk.spyglass_script import Spyglass

url = 'wss://ui.getlore.io/storyteller'
user = 'maurin'
pwd = 'MA123$%'

spyglass = Spyglass(url, user, pwd, dataset_id='payu_v3')

tables = ['@transactions_payubiz']

for table in tables:
    results = spyglass.sync_cmd('aql', [
        ''' 'select count(*) from "{table}" where ingestion_date = \\'{date}\\'' '''
                                .format(table=table,
                                        date=time.strftime("%Y-%m-%d")),
        '--json'])
    assert results['data']['series'][0]['data'][0][
               'count'] > 0, "check failed for table : {} ".format(table)
