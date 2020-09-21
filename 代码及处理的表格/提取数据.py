#!/usr/bin/env python
#._*_ coding:utf-8 _*_

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

train= pd.read_csv('result3_csv.csv',encoding='GB2312')
df1 = train.values
df1= np.array(df1)
print(df1[127])