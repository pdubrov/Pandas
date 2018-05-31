import numpy as np
import pandas as pd

#Missing Data
df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})

print(df)

print(df.dropna(thresh=2))

print(df.fillna(value=df.mean( )))

print(df.mean(axis=1))

# Groupby

# Create dataframe
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)

print(df)
print(df.groupby('Company').mean())


print(df.groupby('Company').describe().transpose()['GOOG'])

# concat, merge, join

'''
https://pandas.pydata.org/pandas-docs/stable/merging.html

pandas provides a single function, merge, as the entry point for all standard database join operations between DataFrame objects:

pd.merge is a function in the pandas namespace, and it is also available as a DataFrame instance method, 
with the calling DataFrame being implicitly considered the left object in the join.

The related DataFrame.join method, uses merge internally for the index-on-index and index-on-column(s) 
joins, but joins on indexes by default rather than trying to join on common columns 
(the default behavior for merge). If you are joining on index, you may wish to use DataFrame.join 
to save yourself some typing.


These two function calls are completely equivalent:

left.join(right, on=key_or_keys)
pd.merge(left, right, left_on=key_or_keys, right_index=True, how='left', sort=False)

and these 2

left.join(right, how='inner')
pd.merge(left, right, left_index=True, right_index=True, how='inner');

'''

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})


print(pd.merge(left, right, on=('key1', 'key2')))

right.set_index(['key1', 'key2'], inplace = True)
left.set_index(['key1', 'key2'], inplace = True)
print(left.join(right, how='inner' ))

print(pd.concat([left, right]))

