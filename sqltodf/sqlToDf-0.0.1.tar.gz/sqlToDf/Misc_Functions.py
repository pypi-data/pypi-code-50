import pandas as pd

def Extract_Values(file_location, row_delim, col_delim):
    f = open(file_location, "r")
    contents = f.read()
    records = []
    holder = []
    cache = ''
    for i in range(0, len(contents)):
        if i == 0:
            cache = contents[i]
        else:
            # Field terminator #
            if contents[i] == col_delim:
                holder.append(cache)
                cache = ''

            # If there is no field terminator append the cache #
            if contents[i] != col_delim and contents[i] != row_delim:
                cache = cache + contents[i]
            else:
                if contents[i] == row_delim:
                    # Row terminator#
                    holder.append(cache)
                    cache = ''
                    records.append(holder)
                    holder = []
    print("Attempt Value Creation")
    return records

def Create_Dataframe(records):
    dataframe = pd.DataFrame(records)
    print("Attempt Dataframe Creation")
    return dataframe

# # Extracting column names from the text file #
# def Extract_Features(file_location):
#     features = np.loadtxt(file_location, dtype='str', delimiter='>')
#     features = features[:-1]
#     print("Attempt Feature Creation")
#     return features