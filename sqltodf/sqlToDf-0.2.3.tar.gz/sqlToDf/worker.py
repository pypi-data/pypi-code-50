from subprocess import call
from Helper_functions import Misc_Functions

class bcp_package:
    def __init__(self, query="SELECT * FROM charge", directory=''
                 , host='127.0.0.1', username='SA', password='abc$12345', coldelim=',', rowdelim='>',
                 database='testing', table='charge'):
        directory = directory + table + '.txt'
        self.query = query
        self.dir = directory
        self.host = host
        self.user_name = username
        self.password = password
        self.col_delim = coldelim
        self.row_delim = rowdelim
        self.database_name = database
        self.table_name = table

    def fetch_in_txt(self):
        call(['bcp', self.query, 'queryout', self.dir, '-t', self.col_delim, '-r', self.row_delim,'-c', '-S', self.host, '-d', self.database_name, '-U', self.user_name, '-P', self.password])

    # def fetch_in_txt(self):
    #     call(['bcp', self.query, 'queryout', self.dir, '-t', self.col_delim,'-c', '-S', self.host, '-d', self.database_name, '-U', self.user_name, '-P', self.password])

    def fetch_in_dataframe(self):
        # 01 Fetch from text file and create list of list #
        list_of_rows = Misc_Functions.Extract_Values(self.dir,self.row_delim,self.col_delim)

        # 02 Creating dataframe of the list of list fetched above from a text file #
        dataframe = Misc_Functions.Create_Dataframe(list_of_rows)
        # 03 Return Dataframe #
        return  dataframe

    def Controller(self):
        self.fetch_in_txt()
        dataframe = self.fetch_in_dataframe()
        return dataframe




if __name__=='__main__':
    instance = bcp_package(query='Select * from customers',directory='',coldelim=',',rowdelim='>',password='abc$12345')
    instance.Controller()