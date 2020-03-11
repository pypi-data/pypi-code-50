import csv
import pandas
import os
import difflib

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

def clearDir(dir):
    for path in os.listdir(dir):
        full_path = os.path.join(dir, path)
        if os.path.isfile(full_path):
            os.remove(full_path)

def cmp(f1_path,f2_path,ignore_lines=None):
    if ignore_lines is None:
        ignore_lines = []
    file1 = open(f1_path, 'r', encoding='utf-8')
    file2 = open(f2_path, 'r', encoding='utf-8')
    try:
        f1 = file1.readlines()
        f2 = file2.readlines()
        for ignore in ignore_lines:
            f1.pop(int(ignore))
            f2.pop(int(ignore))
        diff = difflib.ndiff(f1, f2)
        difference = [l for l in diff if l.startswith('+ ') or l.startswith('- ')]
    finally:
        file1.close()
        file2.close()
    return difference