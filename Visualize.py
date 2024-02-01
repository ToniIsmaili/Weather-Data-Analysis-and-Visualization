import matplotlib.pyplot as plt
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
