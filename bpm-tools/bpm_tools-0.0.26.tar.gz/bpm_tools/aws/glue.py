import boto3
import json


# ------------- add_glue_partition ------------------
#
# ---------------------------------------------------------

def add_glue_partition(s3_bucket_name, s3_key, database_name, table_name):


    # get existing partitions from glue-table
    print("Adding partition....", s3_bucket_name, s3_key, database_name, table_name)

    try:
        glue_client = boto3.client('glue')
        response = glue_client.get_partitions(
            DatabaseName=database_name,
            TableName=table_name,
        )
        existing_partitions = []
        for p in response['Partitions']:
            existing_partitions.append(p['Values'])

        # extract the partitions from the new file
        s3_key_parts = s3_key.split('/')
        s3_key_location = '/'.join(s3_key_parts[:-1])
        new_partition = []
        for part in s3_key_parts:
            if '=' in part:
                new_partition.append(part.split('='))
        print(new_partition)

        # check if partition already exist in the table
        # if partition already in the table, return and exit lambda-function
        test_partition = []
        for key, value in new_partition:
            test_partition.append(value)
        if test_partition in existing_partitions:
            print(test_partition, 'already in existing partitions')
            print(existing_partitions)
            return

        print("adding new partition")
        # build the athena query
        athena_query = '''
        ALTER TABLE {} ADD
        '''.format(table_name)
        partition_string = ''
        for key, value in new_partition:
            partition_string += '{} = \'{}\', '.format(key, value)
        partition_string = partition_string[:-2]
        athena_query += 'PARTITION (' + partition_string + ')' + '\n'
        athena_query += 'LOCATION \'s3://{}/{}\''.format(s3_bucket_name, s3_key_location)
        athena_query += ';'
        print(athena_query)

        # run the athena query to add the partition
        athena_client = boto3.client('athena')
        response = athena_client.start_query_execution(
            QueryString = athena_query,
            QueryExecutionContext={
                "Database": database_name
            },
            ResultConfiguration = {
                "OutputLocation": "s3://test-cxense-storage/athena_output"
            }
        )
        print(response)
        return
    except Exception as e:
        print("Glue table not present - crawler setup required", e)
        return


