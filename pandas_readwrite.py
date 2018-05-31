import pandas as pd
from tabulate import tabulate

df = pd.read_csv("C:\Dev\Py\Examples\sample.csv")
df.sort_values
print(df)
print(repr(df))
print(ascii(df))
print(tabulate(df, headers='keys', tablefmt='psql'))


data=pd.read_html( "https://www.championat.com/football/_england/2214/result.html", header=0)
table=data[0]


print(table  )

#top 5 rows
print(table.columns)

print(table.sort_values("2").head(5))

# How many
print(sum(table["2"].apply(lambda name: "Альбион" in name)))