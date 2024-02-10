import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=[1,2,3,4,5]
data_series=pd.Series(data)

summary_stats=data_series.describe()
median=data_series.median()
variance=data_series.var()
std_dev=data_series.std()
range_val=data_series.max()-data_series.min()


plt.boxplot(data_series)
plt.title("Box Plot")
plt.show()


plt.hist(data_series,bins=5,edgecolor='k')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

print(summary_stats)
print(median)
print(variance)
print(std_dev)
print(range_val)