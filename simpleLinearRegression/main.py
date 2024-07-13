import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('homeprices.csv')

reg = linear_model.LinearRegression()
reg.fit(df[['year']],df.perCapitaIncome)

plt.xlabel('year')
plt.ylabel('perCapitaIncome')
plt.scatter(df.year,df.perCapitaIncome,color='red', marker='+')
plt.plot(df.year,reg.predict(df[['year']]),color='blue')
plt.show()

