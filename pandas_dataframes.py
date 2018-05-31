import numpy as np
import pandas as pd

# All rows and columns are series
df = pd.DataFrame(np.random.randn(4,5),
                  [chr(c) for c in list(np.arange(100,104))],
                  [chr(c) for c in list(np.arange(115, 120))])
print(df)

# SELECT COLUMNS
print(df[['t', 'w']])

df['new'] = df['t']+df['w']
print(df)

df1 = df.drop('new', axis = 1 )

print(df1) # no new column
print(df) # still there

df.drop('new', axis = 1, inplace=True )
print(df)

print(df.shape)
#rows - 0 axis, columns - 1 axis

# SELECT ROWS
#by label
print(df.loc["e"]) #returns Series

#by index
print(df.iloc[2]) # returns Series

print(df.loc[['d', 'f'], ['s', 'v']])


print(df[df>0])

print(df.reset_index())

l = 'bu ra ti no'.split()
df ['hto'] = l
print(df.set_index( 'hto' ))