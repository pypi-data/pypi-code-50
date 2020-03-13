import logging
import sys
import boto3
from datetime import datetime

def config_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    sh.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    )
    logger.addHandler(sh)
    return logger

def get_table_details(glue_table_spec):
    return {
        "Name": glue_table_spec.get('Name'),
        "CreateTime": glue_table_spec.get('CreateTime').replace(tzinfo=None),
        "UpdateTime": glue_table_spec.get('UpdateTime').replace(tzinfo=None),
        "UpdatedLatency": datetime.now() - glue_table_spec.get('UpdateTime').replace(tzinfo=None),
        "recordCount": glue_table_spec.get('Parameters').get('recordCount'),
    }

def get_glue_tables(DB_NAME, GLUE_MAX_TABLES_RESULT=100):
    
    glue = boto3.client('glue')

    glue_tables = glue.get_tables(
        DatabaseName=DB_NAME,
        MaxResults=GLUE_MAX_TABLES_RESULT
    )

    full_tables_list = list()

    logging.info("Looping glue results")
    for tb in glue_tables.get('TableList'):
        full_tables_list.append(get_table_details(tb))

    next_token=glue_tables.get('NextToken')
    logging.info("Fetching glue tables for NextToken: {}".format(next_token))

    # glue_tables = glue.get_tables(
    #     DatabaseName=DB_NAME,
    #     MaxResults=GLUE_MAX_TABLES_RESULT,
    #     NextToken=next_token
    # )

    logging.info("Glue database tables count: {}".format(len(full_tables_list)))

    return full_tables_list
