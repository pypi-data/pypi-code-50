from google.cloud import bigquery
import sys
from multiprocessing.dummy import Pool as ThreadPool
import os
from google.cloud.exceptions import NotFound

class BigQuery:
   
    def __init__(self, project_id, dataset, tableName, schema):
        self.client = bigquery.Client()
        self.project_id = project_id
        self.dataset = dataset
        self.tableName = tableName
        self.table_id = '{}.{}.{}'.format(project_id, dataset, tableName)
        self.schema = schema

    def set_data(self, data):
        self.data = data


    def save_to_table_in_chunks(self):
        
        n = 10000

        chunk = [self.data[i * n:(i + 1) * n] for i in range((len(self.data) + n - 1) // n )]

        pool = ThreadPool(len(chunk))
        
        results = pool.map(self._insert_big_query, chunk)
        
        return results


     # Salva no big query
    def _insert_big_query(self, row):
        
        table = self.client.get_table(self.table_id)
        errors = self.client.insert_rows(table, row)
        return errors


    def _has_bigquery_table(self):
        try:
            self.client.get_table(self.table_id)  # Make an API request.
            print(f'Table {self.table_id} existente')
            return True
        except NotFound:
            return False

    def _create_table(self):
        table = bigquery.Table(self.table_id, schema=self.schema)
        table = self.client.create_table(table)

    def _create_partitioned_table(self, dateName):
        table = bigquery.Table(self.table_id, schema=self.schema)
        table.time_partitioning = bigquery.TimePartitioning(
            type_= bigquery.TimePartitioningType.DAY,
            field=dateName
        #     expiration_ms=7776000000,
        )  # 90 days
        table = self.client.create_table(table)
        

    def delete_table(self):
        self.client.delete_table(self.table_id, not_found_ok=True)  # Make an API request.
        print("Deleted table '{}'.".format(self.table_id))
        return True

    def run_query(self, query):
        query_job = self.client.query(query)  # Make an API request.
        return query_job

    def run_script(self, script):
        script_job = self.client.query(script)  # Make an API request.
        return list(script_job.result())

    
    def create_table_if_not_exists(self):
        if self._has_bigquery_table() == False:
            self._create_table()
            print('Table {} created..'.format(self.tableName))
    
    def delete_and_create_table(self):
        self.delete_table()
        self.create_table_if_not_exists()