from dotenv import load_dotenv
import os

from API import GHCND
import Visualize as plot

load_dotenv('.env')

api = GHCND('https://www.ncei.noaa.gov/cdo-web/api/v2/data', os.getenv('API_KEY'))
df = api.make_request(locationid='FIPS:MK', startdate='2023-12-01', enddate='2023-12-30',
                      units='metric', limit='1000', offset='1')

# plot.station_line_plot(df)
# plot.overall_line_plot(df)
# plot.station_scatter_plot(df)
# plot.overall_scatter_plot(df)
# plot.heatmap(df)
plot.bar_plot(df)
