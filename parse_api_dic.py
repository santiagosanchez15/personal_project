import requests

def api_to_data(api_url:str, limit : dict[str:int]) -> list[dict]:
    '''Gets url to fetch from the API and returns a list of dictionaries'''

    fetch_info = requests.get(url=api_url, params=limit) # get the requests object
    fetch_info.raise_for_status() # will raise an error if there was a problem when trying to fetch the webstie content
    data = fetch_info.json() # fetch the data from the response object
    return data['results']
