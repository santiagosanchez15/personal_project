import pandas as pd

def data_to_dataframe(raw_data:list[dict]):
    '''Takes a list of dictionaries from raw data and turns it into a dataframe using pandas'''

    return pd.json_normalize(raw_data) # using json_normilize instead of data_fram elet us work with nested dictionarieso all the information can be seen