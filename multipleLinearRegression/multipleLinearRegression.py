# price = m1 * area + m2 * bedrooms + m3 * age + b

import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv('data.csv')
