import plotly.figure_factory as pf
import csv
import random
import statistics
import pandas as pd

df = pd.read_csv("new.csv")
height = df["Height(Inches)"].to_list()
weight = df["Weight(Pounds)"].to_list()

htmean = statistics.mean(height)
htmedian = statistics.median(height)
htmode = statistics.mode(height)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(htmean, htmedian, htmode))

#fig = pf.create_distplot([height], ["result"], show_hist=False)

wtmean = statistics.mean(weight)
wtmedian = statistics.median(weight)
wtmode = statistics.mode(weight)

wsd = statistics.stdev(weight)
hsd = statistics.stdev(height)
print("STANDARD DEVIATION of height and weight is {}, {} respectively".format(hsd, wsd))


print("Mean, Median and Mode of height is {}, {} and {} respectively".format(wtmean, wtmedian, wtmode))

fig = pf.create_distplot([weight], ["result"], show_hist=False)
fig.show()