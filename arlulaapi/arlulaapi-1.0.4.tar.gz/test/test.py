import sys
sys.path.insert(1, '../arlulaapi')
from arlulaapi import ArlulaSession 

key = "C9qnuCLHIw6drP2g7tt7eK5tLZ5emldjBeGuoMRBqGiCpytqvA06N2QVHxmy"
secret = "ytZvumFVLbPBTyBUfweFcbuBlsNkkY"
arlula_session = ArlulaSession(key, secret)


search_result = arlula_session.search(
    start="2014-01-01",
    res="vlow",
    lat=40.84,
    long=60.15
)

print(search_result)

order = arlula_session.order(
    id=orderId,
    eula="",
    seats=1,
    webhooks=[...],
    emails=[...]
)

## Downloads the resource to the specified filepath
# Optional suppress parameter controls console output
arlula_session.get_resource(
    id=resourceId,
    filepath="downloads/thumbnail.jpg",
    # optional
    suppress="false"
)

order = arlula_session.get_order(
    id="orderId"
)

orders = arlula_session.list_orders()