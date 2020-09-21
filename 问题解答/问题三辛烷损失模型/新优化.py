#!/usr/bin/env python
#._*_ coding:utf-8 _*_



import numpy as np
import pandas as pd

data = pd.read_csv('result4_csv.csv')

X = data[['S-ZORB.PT_6008.DACA'	,'S-ZORB.LC_5101.PV','S-ZORB.CAL_H2.PV'	,'S-ZORB.FT_9302.PV','S-ZORB.LT_3801.DACA','S-ZORB.SIS_TE_2802'	,'S-ZORB.TE_5201.DACA'	,'S-ZORB.TC_2801.PV',	'S-ZORB.FT_2303.DACA'	,'S-ZORB.LC_5001.PV'	,'S-ZORB.CAL.SPEED.PV',	'S-ZORB.FT_1503.TOTALIZERA.PV',	'S-ZORB.FT_1504.TOTALIZERA.PV',	'S-ZORB.LI_2104.DACA'	,'S-ZORB.TE_1107.DACA.PV',	'S-ZORB.TE_6008.DACA.PV'	,'S-ZORB.TE_1101.DACA.PV'	,'S-ZORB.TE_6001.DACA.PV'	,'S-ZORB.TE_1104.DACA.PV'	,'S-ZORB.PDT_2104.PV'	,'S-ZORB.CAL.CANGLIANG.PV'	,'S-ZORB.TE_1106.DACA.PV',	'S-ZORB.TE_1103.DACA.PV'	,'S-ZORB.PC_2401.PIDA.OP'	,'S-ZORB.PC_2401.PIDA.SP',	'S-ZORB.TE_2001.DACA']]
y = data[['h']]

####75%的样本数据被作为训练集，25%的样本被作为测试集。
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X_train, y_train)

print(linreg.intercept_)#输出b
print (linreg.coef_)#输出W

#####模型评价
#模型拟合测试集
y_pred = linreg.predict(X_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print("MSE:",metrics.mean_squared_error(y_test, y_pred))
# 用scikit-learn计算RMSE
print("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

