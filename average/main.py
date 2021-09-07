import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["average"].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def mean():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["average"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 15], mode="lines", name="MEAN"))
    fig.show()
    mean = statistics.mean(mean_list)
    print("Mean of sample :-",mean )
mean()
population_mean = statistics.mean(data)
print("Mean of all:- ", population_mean)

def standard_deviation():
    mean_list = []
    for i in range(0, 1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print("SD of sample:- ", std_deviation)
standard_deviation()
population_sd = statistics.stdev(data)
print("SD of all:- ", population_sd)