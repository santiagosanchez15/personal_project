from parse_api_dic import api_to_data
from compiled_data_into_pandas import data_to_dataframe

def main():
    url : str = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/food-vendors/records"
    fetch_limit: dict[str,int] = {"limit": 5}
    data = api_to_data(url, fetch_limit)
    dataframe = data_to_dataframe(data)
    print(dataframe)

main()
