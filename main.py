from dotenv import load_dotenv
import os

from API import GHCND
import Visualize as plot

# Loads the .env file, where the api key is stored
load_dotenv('.env')

# Create a GHCND object, by passing it the endpoint and api key
api = GHCND('https://www.ncei.noaa.gov/cdo-web/api/v2/data', os.getenv('API_KEY'))

# Making a request to the api, and storing the results in df_one dataframe.
df_one = api.make_request(locationid='FIPS:MK', startdate='2023-12-01', enddate='2023-12-30',
                          units='metric', limit='1000', offset='1')

# Making a request to the api, and storing the results in df_two dataframe.
df_two = api.make_request(locationid='FIPS:MK', startdate='2023-11-01', enddate='2023-11-30',
                          units='metric', limit='1000', offset='1')

# Creating all the plots and saving them in the results folder
plot.station_line_plot(df_one)
plot.overall_line_plot(df_one)
plot.station_scatter_plot(df_one)
plot.overall_scatter_plot(df_one)
plot.heatmap(df_one)
plot.bar_plot(df_one)
plot.violin_plot(df_one)
plot.compare_station_line_plot(df_one, df_two)
plot.compare_overall_line_plot(df_one, df_two)
plot.compare_station_scatter_plot(df_one, df_two)
plot.compare_overall_scatter_plot(df_one, df_two)
plot.compare_heatmap(df_one, df_two)
plot.compare_violin_plot(df_one, df_two)
plot.compare_bar_plot(df_one, df_two)
