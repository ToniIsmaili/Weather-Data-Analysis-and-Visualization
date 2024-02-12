import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Handles the creation of plots
def __create_plot(plot_type, **params):

    if params['data'] is None:
        print("Given DataFrame is None")
        return

    if plot_type == 'heatmap':
        sns.heatmap(params['data'], cmap='viridis', annot=True, fmt='g', cbar_kws={'label': 'Count'})
        plt.xlabel('Temperature Groups (℃)')
        plt.ylabel('Elevation')

    # Check if the plot that we are creating has a hue
    if 'hue' in params:
        # Check what plot we are trying to create, and create it
        if plot_type == 'lineplot':
            sns.lineplot(x=params['x'], y=params['y'], hue=params['hue'], data=params['data'])
        if plot_type == 'scatterplot':
            sns.scatterplot(x=params['x'], y=params['y'], hue=params['hue'], data=params['data'])
        if plot_type == 'barplot':
            sns.barplot(x=params['x'], y=params['y'], hue=params['hue'], data=params['data'])
        if plot_type == 'violinplot':
            sns.violinplot(x=params['x'], y=params['y'], hue=params['hue'], data=params['data'])
    else:
        # Check what plot we are trying to create, and create it
        if plot_type == 'lineplot':
            sns.lineplot(x=params['x'], y=params['y'], data=params['data'])
        if plot_type == 'scatterplot':
            sns.scatterplot(x=params['x'], y=params['y'], data=params['data'])
        if plot_type == 'barplot':
            sns.barplot(x=params['x'], y=params['y'], data=params['data'])
        if plot_type == 'violinplot':
            sns.violinplot(x=params['x'], y=params['y'], data=params['data'])

    # Changes the labels on the x-axis by rotating them by 30 degrees
    plt.tick_params(axis='x', rotation=30)
    # Sets title, if one has been provided
    if 'title' in params:
        plt.title(params['title'])
    # Sets legend label, if one has been provided
    if 'l_title' in params:
        plt.legend(title=params['l_title'])


# Stores the figure in the result folder as png, and then clears all
def __store_figure(filename):
    # Makes sure everything fits in the image
    plt.tight_layout()

    figure = plt.gcf()
    figure.set_size_inches(12, 9)

    plt.savefig(f'results/{filename}.png', dpi=250)

    # Clears figure and axis
    plt.clf()
    plt.cla()


# Draws a line in a plot for each station with their daily average temperature
def station_line_plot(df):
    title = 'Average temperature for each station visualized with line plot'
    __create_plot('lineplot', x='date', y='value', hue='name', data=df, title=title, l_title='Station Names')

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Station line plot')


# Draws two plots (each having their own dataframe), with each one having one line-per-station
# with their daily average temperature
def compare_station_line_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('lineplot', x='date', y='value', hue="name", data=df_one, l_title='Station Names')
    plt.subplot(1, 2, 2)
    __create_plot('lineplot', x='date', y='value', hue="name", data=df_two, l_title='Station Names')

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Compare station line plot')


# Draws one line in a plot, representing the average temperature for all stations
def overall_line_plot(df):
    # Groups all the data by date and gets the mean of the values on the same day
    local_df = df.groupby('date')['value'].mean().reset_index()

    title = 'Overall average temperature visualized with line plot'
    __create_plot('lineplot', x='date', y='value', data=local_df, title=title)

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Overall line plot')


# Draws two plots (each having their own dataframe), each having a line
# representing the average temperature for all stations
def compare_overall_line_plot(df_one, df_two):
    # Groups all the data by date and gets the mean of the values on the same day
    df_one = df_one.groupby('date')['value'].mean().reset_index()
    df_two = df_two.groupby('date')['value'].mean().reset_index()

    plt.subplot(1, 2, 1)
    __create_plot('lineplot', x='date', y='value', data=df_one)
    plt.subplot(1, 2, 2)
    __create_plot('lineplot', x='date', y='value', data=df_two)

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Compare overall line plot')


# Draws a plot, where each color represents a station and the temperatures are
# represented as dots in a grid
def station_scatter_plot(df):
    title = 'Average temperature for each station visualized with scatter plot'
    __create_plot('scatterplot', x='date', y='value', hue='name', data=df, title=title, l_title='Station Names')

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Station scatter plot')


# Draws two plots (each having their own dataframe), representing
# the values with dots
def compare_station_scatter_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('scatterplot', x='date', y='value', hue='name', data=df_one, l_title='Station Names')
    plt.subplot(1, 2, 2)
    __create_plot('scatterplot', x='date', y='value', hue='name', data=df_two, l_title='Station Names')

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Compare station scatter plot')


# Draws a plot, where all the stations are grouped and the values are averaged,
# and they represented with dots
def overall_scatter_plot(df):
    # Groups all the data by date and gets the mean of the values on the same day
    local_df = df.groupby('date')['value'].mean().reset_index()

    title = 'Overall average temperature visualized with scatter plot'
    __create_plot('scatterplot', x='date', y='value', data=local_df, title=title)

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Overall scatter plot')


# Draws two plots (each having their own dataframe), each of them representing
# the average temperature from all stations with dots
def compare_overall_scatter_plot(df_one, df_two):
    # Groups all the data by date and gets the mean of the values on the same day
    df_one = df_one.groupby('date')['value'].mean().reset_index()
    df_two = df_two.groupby('date')['value'].mean().reset_index()

    plt.subplot(1, 2, 1)
    __create_plot('scatterplot', x='date', y='value', data=df_one)
    plt.subplot(1, 2, 2)
    __create_plot('scatterplot', x='date', y='value', data=df_two)

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Compare overall scatter plot')


# Creates a pivot table used in creating heatmaps
def __create_pivot(df):
    # Making a copy of the dataframe to avoid changing the original dataframe
    local_df = df.copy()

    # Deleting unnecessary columns
    del local_df['date']
    del local_df['name']

    # Creates a range of temperatures, the size of bin_size (ex 0-5, 5-10, 10-15...)
    min_temp = local_df['value'].min()
    max_temp = local_df['value'].max()
    bin_size = 5
    temp_bins = range(int(min_temp // bin_size) * bin_size, int((max_temp // bin_size) + 1) * bin_size, bin_size)

    # Creates a column with each value being assigned a temperature range
    local_df['temp_group'] = pd.cut(local_df['value'], bins=temp_bins, right=False)

    # Turns dataframe into pivot table and returns it
    return local_df.pivot_table(index='elevation', columns='temp_group', aggfunc=len, fill_value=0, observed=True)


# Draws a heatmap, showing the relationship between elevation and the temperature
def heatmap(df):
    title = 'Heatmap of Elevation and Temperature Groups'
    __create_plot('heatmap', data=__create_pivot(df), title=title)

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Heatmap plot')


# Draws two heatmaps (each having their own dataframe), showing the difference
# inbetween elevation and temperature
def compare_heatmap(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('heatmap', data=__create_pivot(df_one))
    plt.subplot(1, 2, 2)
    __create_plot('heatmap', data=__create_pivot(df_two))

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Compare heatmap plot')


# Aggregate function used to return the first mode in the group if not emtpy
def __mode(group):
    return group.mode().iloc[0] if not group.mode().empty else 0


# Extracts the mean, mode, median, min and max values and return dataframe containing that information
def __extract_values(df):
    # Extracts the mean
    mean_df = df.groupby('name')['value'].mean().reset_index()
    mean_df['datatype'] = 'mean'
    # Extracts the mode
    mode_df = df.groupby('name')['value'].agg(__mode).reset_index()
    mode_df['datatype'] = 'mode'
    # Extracts the median
    median_df = df.groupby('name')['value'].median().reset_index()
    median_df['datatype'] = 'median'
    # Extracts the min
    min_df = df.groupby('name')['value'].min().reset_index()
    min_df['datatype'] = 'min'
    # Extracts the max
    max_df = df.groupby('name')['value'].max().reset_index()
    max_df['datatype'] = 'max'
    # Combines them all in one dataframe and returns it
    return pd.concat([mean_df, mode_df, median_df, min_df, max_df])


# Draws plot, that represent the mean, mode, median, min, max of the stations using bar plot
def bar_plot(df):
    title = 'Station mean, mode, median, min, max visualized with bar plot'
    __create_plot('barplot', x='name', y='value', hue='datatype', data=__extract_values(df), title=title)

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Bar plot')


# Draws two plots (each having their own dataframe), each representing mean, mode, median, min, max of the stations
def compare_bar_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('barplot', x='name', y='value', hue='datatype', data=__extract_values(df_one))
    plt.subplot(1, 2, 2)
    __create_plot('barplot', x='name', y='value', hue='datatype', data=__extract_values(df_two))

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Compare bar plot')


# Draws plots, that represents the temperature of each station using a violin shape
def violin_plot(df):
    title = 'Station temperature visualized with violin plot'
    __create_plot('violinplot', x='name', y='value', data=df, title=title)

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Violin plot')


# Draws two plots (each having their own dataframe), used to compair the temperatures with
# the violin shapes
def compare_violin_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('violinplot', x='name', y='value', data=df_one)
    plt.subplot(1, 2, 2)
    __create_plot('violinplot', x='name', y='value', data=df_two)

    # Stores the figure in the result folder as png, and then clears all
    __store_figure('Compare violin plot')
