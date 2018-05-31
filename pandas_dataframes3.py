import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df)
print(df.head())

print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

# Applying functions
def times2(x):
    return x*2

print(df.apply(times2))
print(df.apply(lambda x:x*2))
print(df.apply(len))
print(df.sum())

#Removing column

del df["col3"]
df["col4"] = [ 90, 91, 92, 93]
print(df)
df = df.drop("col4", axis=1)
print(df)

print(df.columns)
print(df.index)

#sort
print(df.sort_values(by='col2'))
print(df.isnull())
df["col5"] = [ 1, None, None, 4]
print(df)
print(df.dropna())

#pivot
data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))

