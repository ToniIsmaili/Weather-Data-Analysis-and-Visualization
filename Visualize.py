import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Handles the creation of plots
def __create_plot(plot_type, **params):

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

    plt.tick_params(axis='x', rotation=30)
    if 'title' in params:
        plt.title(params['title'])
    if 'l_title' in params:
        plt.legend(params['l_title'])


def station_line_plot(df):
    title = 'Average temperature for each station visualized with line plot'
    __create_plot('lineplot', x='date', y='value', hue='name', data=df, title=title, l_title='Station Names')
    plt.show()


def compare_station_line_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('lineplot', x='date', y='value', hue="name", data=df_one, l_title='Station Names')
    plt.subplot(1, 2, 2)
    __create_plot('lineplot', x='date', y='value', hue="name", data=df_two, l_title='Station Names')
    plt.show()


def overall_line_plot(df):
    title = 'Overall average temperature visualized with line plot'
    local_df = df.groupby('date')['value'].mean().reset_index()
    __create_plot('lineplot', x='date', y='value', data=local_df, title=title)
    plt.show()


def compare_overall_line_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    df_one = df_one.groupby('date')['value'].mean().reset_index()
    __create_plot('lineplot', x='date', y='value', data=df_one)
    plt.subplot(1, 2, 2)
    df_two = df_two.groupby('date')['value'].mean().reset_index()
    __create_plot('lineplot', x='date', y='value', data=df_two)
    plt.show()


def station_scatter_plot(df):
    title = 'Average temperature for each station visualized with scatter plot'
    __create_plot('scatterplot', x='date', y='value', hue='name', data=df, title=title, l_title='Station Names')
    plt.show()


def compare_station_scatter_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('scatterplot', x='date', y='value', hue='name', data=df_one, l_title='Station Names')
    plt.subplot(1, 2, 2)
    __create_plot('scatterplot', x='date', y='value', hue='name', data=df_two, l_title='Station Names')
    plt.show()


def overall_scatter_plot(df):
    title = 'Overall average temperature visualized with scatter plot'
    local_df = df.groupby('date')['value'].mean().reset_index()
    __create_plot('scatterplot', x='date', y='value', data=local_df, title=title)
    plt.show()


def compare_overall_scatter_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    df_one = df_one.groupby('date')['value'].mean().reset_index()
    __create_plot('scatterplot', x='date', y='value', data=df_one)
    plt.subplot(1, 2, 2)
    df_two = df_two.groupby('date')['value'].mean().reset_index()
    __create_plot('scatterplot', x='date', y='value', data=df_two)
    plt.show()


def __create_pivot(df):
    local_df = df.copy()
    del local_df['date']
    del local_df['name']
    # Determine temperature bins dynamically
    min_temp = local_df['value'].min()
    max_temp = local_df['value'].max()
    bin_size = 5
    temp_bins = range(int(min_temp // bin_size) * bin_size, int((max_temp // bin_size) + 1) * bin_size, bin_size)

    # Create temperature groups
    local_df['temp_group'] = pd.cut(local_df['value'], bins=temp_bins, right=False)

    # Create a pivot table for the heatmap
    return local_df.pivot_table(index='elevation', columns='temp_group', aggfunc=len, fill_value=0, observed=True)


def heatmap(df):
    # Create the heatmap using seaborn
    title = 'Heatmap of Elevation and Temperature Groups'
    __create_plot('heatmap', data=__create_pivot(df), title=title)
    plt.show()


def compare_heatmap(df_one, df_two):
    # Create the heatmap using seaborn
    plt.subplot(1, 2, 1)
    __create_plot('heatmap', data=__create_pivot(df_one))
    plt.subplot(1, 2, 2)
    __create_plot('heatmap', data=__create_pivot(df_two))
    plt.show()


def __mode(group):
    return group.mode().iloc[0] if not group.mode().empty else 0


# Extracts the mean, mode, median, min and max values and return dataframe containing that information
def __extract_values(df):
    mean_df = df.groupby('name')['value'].mean().reset_index()
    mean_df['datatype'] = 'mean'
    mode_df = df.groupby('name')['value'].agg(__mode).reset_index()
    mode_df['datatype'] = 'mode'
    median_df = df.groupby('name')['value'].median().reset_index()
    median_df['datatype'] = 'median'
    min_df = df.groupby('name')['value'].min().reset_index()
    min_df['datatype'] = 'min'
    max_df = df.groupby('name')['value'].max().reset_index()
    max_df['datatype'] = 'max'
    return pd.concat([mean_df, mode_df, median_df, min_df, max_df])


def bar_plot(df):
    title = 'Station mean, mode, median, min, max visualized with bar plot'
    __create_plot('barplot', x='name', y='value', hue='datatype', data=__extract_values(df), title=title)
    plt.show()


def compare_bar_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('barplot', x='name', y='value', hue='datatype', data=__extract_values(df_one))
    plt.subplot(1, 2, 2)
    __create_plot('barplot', x='name', y='value', hue='datatype', data=__extract_values(df_two))
    plt.show()


def violin_plot(df):
    title = 'Station temperature visualized with violin plot'
    __create_plot('violinplot', x='name', y='value', data=df, title=title)
    plt.show()


def compare_violin_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    __create_plot('violinplot', x='name', y='value', data=df_one)
    plt.subplot(1, 2, 2)
    __create_plot('violinplot', x='name', y='value', data=df_two)
    plt.show()
