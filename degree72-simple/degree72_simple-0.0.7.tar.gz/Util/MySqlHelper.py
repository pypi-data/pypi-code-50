import pandas as pd
from sqlalchemy import create_engine


class MysqlHelper:
    def __init__(self, *args, **kwargs):
        self.df = pd.DataFrame()
        self.source_mysql_config = kwargs.get('source_mysql_config')
        self.target_mysql_config = kwargs.get('target_mysql_config')

        self.source_engine= create_engine("{dr}://{user}:{password}@{host}:{port}/{database}" \
                                    .format(dr='mysql', **self.source_mysql_config))

        self.target_engine= create_engine("{dr}://{user}:{password}@{host}:{port}/{database}" \
                                          .format(dr='mysql', **self.target_mysql_config))

    def csv_to_mysql(self, input_file_name):
        self.get_data_from_csv(input_file_name)
        self.export_data_to_mysql()
        pass

    def mysql_to_csv(self, sql_input, output_file_name):
        self.get_data_from_mysql(sql_input)
        self.export_data_to_csv(output_file_name)

    def mysql_to_mysql(self, input_sql):
        self.get_data_from_mysql(input_sql=input_sql)
        self.export_data_to_mysql()

    def get_data_from_csv(self, file_name):
        self.df = pd.read_csv(file_name, index_col=None)

    def get_data_from_mysql(self, input_sql):
        with self.source_engine.connect() as conn, conn.begin():
            self.df = pd.read_sql(sql=input_sql, con=conn, index_col=None)

    def export_data_to_csv(self, target_file_name):
        self.df.to_csv(target_file_name)
        pass

    def export_data_to_mysql(self):
        table_name = self.target_mysql_config['table_name']
        with self.target_engine.connect() as conn, conn.begin():
            self.df.to_sql(table_name, conn, if_exists='append', index=False)

