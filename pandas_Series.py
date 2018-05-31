import numpy as np
import pandas as pd

series = pd.Series( [1,5,3], ["o", "i", "d"])
print(series)

print(series.autocorr(1))
