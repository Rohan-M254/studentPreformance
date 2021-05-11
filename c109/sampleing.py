import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
df=pd.read_csv("newdata.csv")
data=df["temp"].tolist()
population_mean=statistics.mean(data)
fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.show()