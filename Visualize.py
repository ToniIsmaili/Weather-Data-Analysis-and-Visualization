import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def station_line_plot(df):
    sns.lineplot(x='date', y='value', hue="name", data=df)
    plt.tick_params(axis='x', rotation=30)
    plt.legend(title='Station Names')
    plt.title('Average temperature for each station visualized with line plot')
    plt.show()


def compare_station_line_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    sns.lineplot(x='date', y='value', hue="name", data=df_one)
    plt.tick_params(axis='x', rotation=30)
    plt.legend(title='Station Names')
    plt.subplot(1, 2, 2)
    sns.lineplot(x='date', y='value', hue="name", data=df_two)
    plt.tick_params(axis='x', rotation=30)
    plt.legend(title='Station Names')
    plt.show()


def overall_line_plot(df):
    df = df.groupby('date')['value'].mean().reset_index()
    sns.lineplot(x='date', y='value', data=df)
    plt.tick_params(axis='x', rotation=30)
    plt.title('Overall average temperature visualized with line plot')
    plt.show()


def compare_overall_line_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    df_one = df_one.groupby('date')['value'].mean().reset_index()
    sns.lineplot(x='date', y='value', data=df_one)
    plt.tick_params(axis='x', rotation=30)
    plt.subplot(1, 2, 2)
    df_two = df_two.groupby('date')['value'].mean().reset_index()
    sns.lineplot(x='date', y='value', data=df_two)
    plt.tick_params(axis='x', rotation=30)
    plt.show()


def station_scatter_plot(df):
    sns.scatterplot(x='date', y='value', hue='name', data=df)
    plt.legend(title='Station Names')
    plt.tick_params(axis='x', rotation=30)
    plt.title('Average temperature for each station visualized with scatter plot')
    plt.show()


def compare_station_scatter_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    sns.scatterplot(x='date', y='value', hue='name', data=df_one)
    plt.legend(title='Station Names')
    plt.tick_params(axis='x', rotation=30)
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='date', y='value', hue='name', data=df_two)
    plt.legend(title='Station Names')
    plt.tick_params(axis='x', rotation=30)
    plt.show()


def overall_scatter_plot(df):
    df = df.groupby('date')['value'].mean().reset_index()
    sns.scatterplot(x='date', y='value', data=df)
    plt.tick_params(axis='x', rotation=30)
    plt.title('Overall average temperature visualized with scatter plot')
    plt.show()


def compare_overall_scatter_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    df_one = df_one.groupby('date')['value'].mean().reset_index()
    sns.scatterplot(x='date', y='value', data=df_one)
    plt.tick_params(axis='x', rotation=30)
    plt.subplot(1, 2, 2)
    df_two = df_two.groupby('date')['value'].mean().reset_index()
    sns.scatterplot(x='date', y='value', data=df_two)
    plt.tick_params(axis='x', rotation=30)
    plt.show()


def heatmap(df):
    del df['date']
    del df['name']
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


def compare_heatmap(df_one, df_two):
    del df_one['date']
    del df_one['name']

    del df_two['date']
    del df_two['name']
    # Determine temperature bins dynamically
    min_temp_one = df_one['value'].min()
    max_temp_one = df_one['value'].max()
    min_temp_two = df_two['value'].min()
    max_temp_two = df_two['value'].max()
    bin_size = 5
    bins_one = range(int(min_temp_one // bin_size) * bin_size, int((max_temp_one // bin_size) + 1) * bin_size, bin_size)
    bins_two = range(int(min_temp_two // bin_size) * bin_size, int((max_temp_two // bin_size) + 1) * bin_size, bin_size)

    # Create temperature groups
    df_one['temp_group'] = pd.cut(df_one['value'], bins=bins_one, right=False)
    df_two['temp_group'] = pd.cut(df_two['value'], bins=bins_two, right=False)

    # Create a pivot table for the heatmap
    pivot_one = df_one.pivot_table(index='elevation', columns='temp_group', aggfunc=len, fill_value=0, observed=True)
    pivot_two = df_two.pivot_table(index='elevation', columns='temp_group', aggfunc=len, fill_value=0, observed=True)

    # Create the heatmap using seaborn
    plt.subplot(1, 2, 1)
    sns.heatmap(pivot_one, cmap='viridis', annot=True, fmt='g', cbar_kws={'label': 'Count'})
    plt.tick_params(axis='x', rotation=15)
    plt.xlabel('Temperature Groups (℃)')
    plt.ylabel('Elevation')
    plt.subplot(1, 2, 2)
    sns.heatmap(pivot_two, cmap='viridis', annot=True, fmt='g', cbar_kws={'label': 'Count'})
    plt.tick_params(axis='x', rotation=15)
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


def compare_bar_plot(df_one, df_two):
    mean_df_one = df_one.groupby('name')['value'].mean().reset_index()
    mean_df_one['datatype'] = 'mean'
    mode_df_one = df_one.groupby('name')['value'].agg(__mode).reset_index()
    mode_df_one['datatype'] = 'mode'
    median_df_one = df_one.groupby('name')['value'].median().reset_index()
    median_df_one['datatype'] = 'median'
    min_df_one = df_one.groupby('name')['value'].min().reset_index()
    min_df_one['datatype'] = 'min'
    max_df_one = df_one.groupby('name')['value'].max().reset_index()
    max_df_one['datatype'] = 'max'
    df_one = pd.concat([mean_df_one, mode_df_one, median_df_one, min_df_one, max_df_one])

    mean_df_two = df_two.groupby('name')['value'].mean().reset_index()
    mean_df_two['datatype'] = 'mean'
    mode_df_two = df_two.groupby('name')['value'].agg(__mode).reset_index()
    mode_df_two['datatype'] = 'mode'
    median_df_two = df_two.groupby('name')['value'].median().reset_index()
    median_df_two['datatype'] = 'median'
    min_df_two = df_two.groupby('name')['value'].min().reset_index()
    min_df_two['datatype'] = 'min'
    max_df_two = df_two.groupby('name')['value'].max().reset_index()
    max_df_two['datatype'] = 'max'
    df_two = pd.concat([mean_df_two, mode_df_two, median_df_two, min_df_two, max_df_two])

    plt.subplot(1, 2, 1)
    sns.barplot(x='name', y='value', hue='datatype', data=df_one)
    plt.tick_params(axis='x', rotation=30)
    plt.subplot(1, 2, 2)
    sns.barplot(x='name', y='value', hue='datatype', data=df_two)
    plt.tick_params(axis='x', rotation=30)
    plt.show()


def violin_plot(df):
    sns.violinplot(x='name', y='value', data=df)
    plt.tick_params(axis='x', rotation=30)
    plt.title('Station temperature visualized with violin plot')
    plt.show()


def compare_violin_plot(df_one, df_two):
    plt.subplot(1, 2, 1)
    sns.violinplot(x='name', y='value', data=df_one)
    plt.tick_params(axis='x', rotation=30)
    plt.subplot(1, 2, 2)
    sns.violinplot(x='name', y='value', data=df_two)
    plt.tick_params(axis='x', rotation=30)
    plt.show()
