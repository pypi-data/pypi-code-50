import csv
import pandas

def getCellValueFromCSV(filepath,delim,row,col):
    with open(filepath, 'r', encoding='utf-8') as temp_f:
        data = csv.reader(temp_f,delimiter=delim)
        data = list(data)
        return str(data[row][col])



def getCellValueFromPivot(filepath,delim,row,col):
    largest_column_count = 0
    with open(filepath, 'r',encoding='utf-8') as temp_f:
        # Read the lines
        lines = temp_f.readlines()
        for l in lines:
            # Count the column count for the current line
            column_count = len(l.split(delim)) + 1

            # Set the new most column count
            largest_column_count = column_count if largest_column_count < column_count else largest_column_count
    temp_f.close()
    column_names = [i for i in range(0, largest_column_count)]
    # Read csv
    df = pandas.read_csv(filepath, header=None, delimiter=delim, names=column_names)
    return str(df[col][row])