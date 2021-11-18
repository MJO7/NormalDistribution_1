import statistics as st
from numpy import False_
import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff
df = pd.read_csv('StudentsPerformance.csv')
readingScore = df["reading score"].to_list()

readingMean = st.mean(readingScore)
readingMedian = st.median(readingScore)
readingMode = st.mode(readingScore)

print("Mean is" , readingMean)
print("Mode is" , readingMode)
print("Median is" , readingMedian)

readingStdev = st.stdev(readingScore)

print("Standard Deviation is" , readingStdev)

first_stdev_start , first_stdev_end = readingMean-readingStdev , readingMean+readingStdev
second_stdev_start , second_stdev_end = readingMean-(2*readingStdev) , readingMean+(2*readingStdev)
third_stdev_start , third_stdev_end = readingMean-(3*readingStdev) , readingMean+(3*readingStdev)

data_1_stdev =  [result for result in readingScore if result > first_stdev_start and result < first_stdev_end]
data_2_stdev =  [result for result in readingScore if result > second_stdev_start and result < second_stdev_end]
data_3_stdev =  [result for result in readingScore if result > third_stdev_start and result < third_stdev_end]

print("{}% of data of height within one Standard Deviation".format(len(data_1_stdev)*100.0/len(readingScore)))
print("{}% of data of height within two Standard Deviation".format(len(data_2_stdev)*100.0/len(readingScore)))
print("{}% of data of height within three Standard Deviation".format(len(data_3_stdev)*100.0/len(readingScore)))

fig = ff.create_distplot([readingScore] , ["Score"] , show_hist=False)
fig.show()