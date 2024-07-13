# price = m1 * area + m2 * bedrooms + m3 * age + b

import pandas as pd
from sklearn import linear_model
import math as m

df = pd.read_csv('homeprices.csv')
print(df)
average = m.floor(df.bedrooms.median())
print(average)
df.bedrooms = df.bedrooms.fillna(average)
print(df)


reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df.price)
for i in reg.coef_:
    print(i)

print(reg.intercept_)

predict1 = reg.predict([[3000, 3, 40]])
print(predict1)

predict2 = reg.predict([[2500, 4, 5]])
print(predict2)

