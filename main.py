from parse_api_dic import api_to_data

def main():
    url : str = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/food-vendors/records"
    fetch_limit: dict[str,int] = {"limit": 100}
    data = api_to_data(url, fetch_limit)
    print(data)

main()
