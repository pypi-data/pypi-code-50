import json
from .utils import config_logger, get_glue_tables

# Loading logger config from aux function
logging = config_logger()

def get_tables(catalog_name, max_latency_days=1):

    logging.info("Retrieving information for catalog [ {} ]".format(catalog_name))

    tables_list = get_glue_tables(catalog_name)

    result = {
        "outdated": 0,
        "updated": 0,
        "outdated_list": []
    }
    for table in tables_list:
        table_days_updated = table.get('UpdatedLatency').days
        if table_days_updated > max_latency_days:
            result['outdated'] += 1
            result['outdated_list'].append({
                "table_name": table.get('Name'),
                "due_days": table_days_updated,
                "rows": table.get('recordCount'),
                "last_updated": table.get('UpdateTime'),
            })
            logging.debug("Table {} has latency greather than alowed ({} x {})".format(table.get('Name'), table_days_updated, max_latency_days))
        else:
            result['updated'] += 1

    logging.info("Glue catalog check results:")
    return json.dumps(result, indent=2, default=str)