from parse_api_dic import api_to_data
from compiled_data_into_pandas import data_to_dataframe

def main():
    url : str = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/food-vendors/records" # thats the given url but any otherone may work
    fetch_limit: dict[str,int] = {"limit": 5}
    data = api_to_data(url, fetch_limit) #get tdata in json format
    dataframe = data_to_dataframe(data) #get data in json_normalizer format, tabulated
    print(dataframe)

main()
