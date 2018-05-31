import numpy as np
import pandas as pd

# 1. Load from csv
df1 = pd.read_csv("C:\Dev\Py\Kaggle\datasets\\football-matches-of-spanish-league\FMEL_Dataset.csv")
print("dataset1")
print(df1.size)
print(df1.head(10))


# 2. Create from numpy array
df2 = pd.DataFrame(np.random.randn(4,5))
print("dataset2")
print(df2.size)
print(df2.head(10))


# 3. Create from numpy array providing index and columns
df3 = pd.DataFrame(np.random.randn(4,5),
                  [chr(c) for c in list(np.arange(100,104))],  # index
                  [chr(c) for c in list(np.arange(115, 120))]) # columns
print("dataset3")
print(df3.size)
print(df3.head(10))

#4. Create from dictionary
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df4 = pd.DataFrame(data)
print("dataset4")
print(df4.size)
print(df4.head(10))
