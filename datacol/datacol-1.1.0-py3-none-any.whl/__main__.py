# Globals
dbr = None
dbw = None
dbl = None
work = None
file_name = None
# DataColError Class
class DataColError:
    def __init__(self, arg):
        self.strerr = arg
        self.arg = {arg}

# NewDB Class
class NewDB:
    def __init__(self, file_namek):
        global dbr
        global dbl
        global dbw
        global file_name
        if file_namek[-3:-1] != '.db':
            raise DataColError('Invalid File (File must have a .db extension).')
        file_name = file_namek
        dbr = open(file_name, "r")
        dbw = open(file_name, "a")
        dbl = dbr.readlines()
    def query(self, val, param):
        for line in dbl:
            linetype = line[0:4]
            equal = line.find("=")
            namespace = equal - 1
            valuespace = equal + 1
            if linetype == "nvp;" and val == "nvp":
                    name = line[5:namespace]
                    value = line[valuespace::]
                    if param == name:
                        return value
        elif linetype == "vlu;" and val == "vlu":
            value = line[5::]
            if value == param:
                return True
            else:
                return False
    def insert(self, val, param):
        global dbw
        global dbl
        global dbr
        if val == "nvp":
        if dbl[-1] != "":
            content = "\nnvp; " + param
        else:
            content = "nvp;" + param + "\n"
        if "=" not in param:
            raise DataColError('Invalid Parameter')
        else:
            dbw.write(content)
            dbr = open(file_name, "r")
            dbl = dbr.readlines()
        elif val == "vlu":
        if dbl[-1] != "":
            content = "\nvlu; " + param
        else:
            content = "vlu; " + param + "\n"
        dbw.write(content)
        dbl = dbr.readlines()

# Help Function
def help():
  print("Welcome to DataCol!")
  print("You can create a new database using the \"NewDB\" class. It takes only one parameter: the name of the file to be used as the database.")
  print("You can search the database using the \"query\" method. This takes 2 parameters: the kind of data you are looking for, and the keywords to search for.")
  print("You can insert data into the database using the insert function. This takes the same parameters as the query method: the kind of data to insert, and the data to insert.")
  print("For more information, visit https://repl.it/@ekholmes/datacol or https://github.com/EKHolmes/DataCol.")
