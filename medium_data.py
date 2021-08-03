import pandas as pd
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def getSampleAverage(number):
    samples=[]
    for i in range(1,number):
        a=random.randint(0,len(data)-1)
        b=data[a]
        samples.append(b)
    c=statistics.mean(samples)
    return(c)

def averageOfSampleAverages():
    allAverages=[]
    for i in range(1,100):
         x = getSampleAverage(100)
         allAverages.append(x)
    averageOfAverages=statistics.mean(allAverages)
    print(averageOfAverages)

averageOfSampleAverages()