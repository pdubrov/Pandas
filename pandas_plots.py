import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
df.plot.area
df.plot.barh
df.plot.density
df.plot.hist
df.plot.line
df.plot.scatter
df.plot.bar
df.plot.box
df.plot.hexbin
df.plot.kde
df.plot.pie
'''

df = pd.read_csv("C:\Dev\Py\Udemy-Python For Finance\
                  Python-for-Finance-Repo-master\\04-Visualization-Matplotlib-Pandas\
                  04-02-Pandas Visualization\df2.csv")
print(df.head())

plt.style.use('ggplot')

df.plot.area(alpha=0.4)

plt.show()