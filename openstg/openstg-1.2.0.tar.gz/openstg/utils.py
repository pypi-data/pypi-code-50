from ast import literal_eval

from flask_restful import reqparse
from datetime import datetime
import pytz

class ArgumentsParser(object):

    @staticmethod
    def parse():
        parser = reqparse.RequestParser()
        parser.add_argument(
            'filter', dest='filter',
            type=str, help='Filter for searching items'
        )
        parser.add_argument(
            'schema', dest='schema',
            type=str, help='Schema for dumping the JSON'
        )
        parser.add_argument(
            'limit', dest='limit', default=10,
            type=int, help='Limit results'
        )
        parser.add_argument(
            'offset', dest='offset', default=0,
            type=int, help='Offset of results'
        )
        args = parser.parse_args()
        limit = args.limit
        offset = args.offset
        search_params = []
        if args.filter:
            try:
                search_params = literal_eval(args.filter)
            except (ValueError, SyntaxError) as e:
                raise
        return search_params, limit, offset


def get_season(dt):
    utc = pytz.timezone('UTC')
    query_date = utc.localize(datetime.strptime(dt, "%Y%m%d%H%M%S"))
    local_tz = pytz.timezone('Europe/Madrid')
    local_time = query_date.astimezone(local_tz)
    if local_time.dst().seconds > 0:
        return 'S'
    else:
        return 'W'
