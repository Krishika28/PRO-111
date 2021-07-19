  
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random
import pandas as pd

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

mean = s.mean(data)

def random_sample(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = s.mean(df)
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()


def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_sample(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = s.mean(mean_list)
    print("Mean of sampling distribution :-",mean )


mean_list = []

for i in range(0,1000):
    m = random_sample()
    mean_list.append(m)

sample_mean = s.mean(mean_list)
stdev = s.stdev(mean_list)


setup()


population_mean = s.mean(data)
print("population mean:- ", population_mean)


def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_sample(100)
        mean_list.append(set_of_means)

    std_deviation = s.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

print("mean of sampling distribution: ",sample_mean)
print("Standard Devation of sampling distribution: ",stdev)

zScore = (sample_mean-mean)/stdev
print("Z Score of inteventation",zScore)


standard_deviation()