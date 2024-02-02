import requests
import pandas as pd


class GHCND:
    url = None
    headers = None

    # Constructor setting the endpoint and the api key
    def __init__(self, url, api_key):
        self.headers = {'token': api_key}
        self.url = url

    def make_request(self, **params):
        # Set the data set to 'GHCND' and the data type to 'TAVG' (The average temperature during the day)
        params['datasetid'] = 'GHCND'
        params['datatypeid'] = 'TAVG'

        # Make a request to the api
        response = requests.get(self.url, params=params, headers=self.headers).json()

        # If we get a response save it to a dataframe and delete unnecessary columns
        if 'results' in response:
            df = pd.DataFrame(response['results'])
            del df['attributes']
            del df['datatype']
            # Format date to YYYY-MM-DD format
            df['date'] = pd.to_datetime(df['date']).dt.date
            # Returns dataframe with all necessary information
            return self.__rename_station(df, params['locationid'])

    # Rename values in the column station, from id to name (GHCND:MK000013577 -> LAZAROPOLE, MK)
    def __rename_station(self, df, locationid):
        # Station endpoint where the data for station names is located
        url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/stations'
        params = {'locationid': locationid}

        # Make a request to the api
        response = requests.get(url, params=params, headers=self.headers).json()

        # If we get a response save it to a dataframe
        if 'result' in response:
            station_df = pd.DataFrame(response['results'])
            # Delete unnecessary columns
            station_df = station_df.drop(['mindate', 'maxdate', 'latitude', 'longitude',
                                          'datacoverage', 'elevationUnit'], axis=1)
            # Merge the dataframes based on station ids
            return pd.merge(df, station_df, left_on='station', right_on='id').drop(['id', 'station'], axis=1)
