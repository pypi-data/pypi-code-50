
import decimal
import json
#Required to to convert the incoming json event to decimal (DynamoDB does not accept floating point!)
from decimal import Decimal

# ------------- Create batches of size = size from a list------------------
#
#  Takes a list and returns a generator
# ---------------------------------------------------------------------

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)