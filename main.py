import requests
import pandas as pd
from dotenv import load_dotenv
import os


class API:
    df = None
    url = None
    headers = None

    def __init__(self, url, api_key):
        self.headers = {'token': api_key}
        self.url = url

    def make_request(self, **params):
        response = requests.get(self.url, params=params, headers=self.headers).json()

        if 'results' in response:
            # Convert the 'results' to a DataFrame
            self.df = pd.DataFrame(response['results'])


load_dotenv('.env')

api = API('https://www.ncei.noaa.gov/cdo-web/api/v2/data', os.getenv('API_KEY'))
api.make_request(datasetid='GHCND', locationid='FIPS:MK', startdate='2023-12-01', enddate='2023-12-30',
                 datatypeid='TMAX', units='metric', limit='1000')
print(api.df)
