import pandas as pd
import csv
import plotly_express as px
import plotly.figure_factory as ff
import random

df = pd.read_csv('./csv/mobile.csv')

fig = ff.create_distplot([df['Avg Rating'].tolist()],['Rating'], show_hist = False)
fig.show()