# Loading data using seaborn data

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression

data = sb.load_dataset("titanic")
df = pd.DataFrame(data)
dataf = df.rename(columns = str.title)
print(dataf.head())
plt.hist('df',bins = 30)
plt.show()

