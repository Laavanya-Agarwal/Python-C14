import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def mean():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["publication"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 15], mode="lines", name="MEAN"))
    fig.show()
    mean = statistics.mean(mean_list)
    print("Population mean: ",mean )
mean()
population_mean = statistics.mean(data)
print("Sampling mean: ", population_mean)