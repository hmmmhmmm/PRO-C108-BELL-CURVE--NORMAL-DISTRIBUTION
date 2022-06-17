import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.readcsv("data.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["rating"])
fig.show()