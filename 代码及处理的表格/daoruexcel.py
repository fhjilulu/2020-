#!/usr/bin/env python
#._*_ coding:utf-8 _*_
#附件一：325个样本数据.xlsx
import pandas as pd
import numpy as np

df=pd.read_excel('sample_1245.xlsx',encoding='utf-8')
height,width = df.shape

a = np.zeros((height-2,width-2))
for i in range(2,height):
    for j in range(2,width):
        a[i-2,j-2] = df.iloc[i,j]
print(a.shape)

a_labels=[]
for i in range(2,width):
    a_labels.append(df.iloc[0, i])

print(len(a_labels))

dt = pd.DataFrame(a, columns=a_labels)
dt.to_csv("result_csv.csv", index=0)