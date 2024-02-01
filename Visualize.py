import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def station_line_plot(df):
    sns.lineplot(x='date', y='value', hue="name", data=df)
    plt.tick_params(axis='x', rotation=30)
    plt.legend(title='Station Names')
    plt.title('Average temperature for each station visualized with line plot')
    plt.show()


def overall_line_plot(df):
    df = df.groupby('date')['value'].mean().reset_index()
    sns.lineplot(x='date', y='value', data=df)
    plt.tick_params(axis='x', rotation=30)
    plt.title('Overall average temperature visualized with line plot')
    plt.show()


def station_scatter_plot(df):
    sns.scatterplot(x='date', y='value', hue='name', data=df)
    plt.legend(title='Station Names')
    plt.tick_params(axis='x', rotation=30)
    plt.title('Average temperature for each station visualized with scatter plot')
    plt.show()


def overall_scatter_plot(df):
    df = df.groupby('date')['value'].mean().reset_index()
    sns.scatterplot(x='date', y='value', data=df)
    plt.tick_params(axis='x', rotation=30)
    plt.title('Overall average temperature visualized with scatter plot')
    plt.show()


def heatmap(df):
    del df['date']
    del df['name']
    df['temp_group'] = pd.cut(df['value'], bins=range(0, 16, 5), right=False)
    df.to_csv('heatmap.csv')
    # Determine temperature bins dynamically
    min_temp = df['value'].min()
    max_temp = df['value'].max()
    bin_size = 5
    temp_bins = range(int(min_temp // bin_size) * bin_size, int((max_temp // bin_size) + 1) * bin_size, bin_size)

    # Create temperature groups
    df['temp_group'] = pd.cut(df['value'], bins=temp_bins, right=False)

    # Create a pivot table for the heatmap
    heatmap_data = df.pivot_table(index='elevation', columns='temp_group', aggfunc=len, fill_value=0, observed=True)

    # Create the heatmap using seaborn
    sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt='g', cbar_kws={'label': 'Count'})
    plt.title('Heatmap of Elevation and Temperature Groups')
    plt.xlabel('Temperature Groups (℃)')
    plt.ylabel('Elevation')
    plt.show()


def __mode(group):
    return group.mode().iloc[0] if not group.mode().empty else 0


def bar_plot(df):
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
    df = pd.concat([mean_df, mode_df, median_df, min_df, max_df])
    sns.barplot(x='name', y='value', hue='datatype', data=df)
    plt.tick_params(axis='x', rotation=30)
    plt.title('Station mean, mode, median, min, max visualized with bar plot')
    plt.show()
