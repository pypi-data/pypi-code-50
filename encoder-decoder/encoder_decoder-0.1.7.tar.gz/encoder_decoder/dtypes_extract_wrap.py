#########################################################################################################################################################
########## OUR CONVENTION OF POSITIONING DATA IN REQUESTS AND RESPONSES WILL BE RECODED IN THESE extract_input and wrap_output functions ################
#########################################################################################################################################################

DATA = 'data'

def wrap_data(data, di):
    di[DATA] = data
    return di

def extract_data(di):
    return di[DATA]