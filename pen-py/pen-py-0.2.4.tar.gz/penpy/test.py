from dicplus import DicPlus

json_dp = DicPlus.from_json('example_request.json')

for i in json_dp.search("included[?type == 'flows'].meta.\"pnbx:end-user:notif\".templates"):
    i.pprint()