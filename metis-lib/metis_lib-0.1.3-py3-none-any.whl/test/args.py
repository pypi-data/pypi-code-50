
from metis_lib import args, utils, result

metis_args = args.loads({
    'path': '/app/dmp_pi/metis_worker/spark',
    'hive_path': '',

    'date_basis': 'today',
    'push_start_dt': '',
    'user_start_dt': '',
    'ocb_start_dt': '',
    'syrup_start_dt': '',
    'card_start_dt': '',
    'coupon_start_dt': '',
    'offline_start_dt': '',
})

print(metis_args)

result(metis_args)