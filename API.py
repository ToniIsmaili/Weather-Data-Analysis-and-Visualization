import requests
import pandas as pd


class GHCND:
    url = None
    headers = None

    def __init__(self, url, api_key):
        self.headers = {'token': api_key}
        self.url = url

    def make_request(self, **params):
        params['datasetid'] = 'GHCND'
        params['datatypeid'] = 'TAVG'
        response = requests.get(self.url, params=params, headers=self.headers).json()

        if 'results' in response:
            # Convert the 'results' to a DataFrame
            df = pd.DataFrame(response['results'])
            del df['attributes']
            del df['datatype']
            df['date'] = pd.to_datetime(df['date']).dt.date
            return self.__rename_station(df, params['locationid'])

    def __rename_station(self, df, locationid):
        url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/stations'
        params = {'locationid': locationid}
        station_df = pd.DataFrame(requests.get(url, params=params, headers=self.headers).json()['results'])
        station_df = station_df.drop(['mindate', 'maxdate', 'latitude', 'longitude', 'datacoverage', 'elevationUnit'], axis=1)
        return pd.merge(df, station_df, left_on='station', right_on='id').drop(['id', 'station'], axis=1)

