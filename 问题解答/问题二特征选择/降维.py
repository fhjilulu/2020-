#!/usr/bin/env python
#._*_ coding:utf-8 _*_

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

train= pd.read_csv('result_csv.csv',encoding='GB2312')
features = train.corr().columns[train.corr()['j'].abs() > .295]
features = features.drop('j')

# 使用随机森林模型进行拟合的过程
X_train = train[features]
y_train = train['j']
feat_labels = X_train.columns

rf = RandomForestRegressor(n_estimators=100, max_depth=None)
rf_pipe = Pipeline([('imputer', SimpleImputer(strategy='median')), ('standardize', StandardScaler()), ('rf', rf)])
rf_pipe.fit(X_train, y_train)

# 根据随机森林模型的拟合结果选择特征
rf = rf_pipe.__getitem__('rf')
importance = rf.feature_importances_

# np.argsort()返回待排序集合从下到大的索引值，[::-1]实现倒序，即最终imp_result内保存的是从大到小的索引值
imp_result = np.argsort(importance)[::-1][:30]


# 按重要性从高到低输出属性列名和其重要性
for i in range(len(imp_result)):
    print("%2d. %-*s %f" % (i + 1, 30, feat_labels[imp_result[i]], importance[imp_result[i]]))

a_labels=[]
a_labels1=[]
for i in range(len(imp_result)):
    a_labels.append(feat_labels[imp_result[i]])
    a_labels1.append(feat_labels[imp_result[i]])
print(a_labels)

# 对属性列，按属性重要性从高到低进行排序
feat_labels = [feat_labels[i] for i in imp_result]
# 绘制特征重要性图像
plt.title('Feature Importance')
plt.bar(range(len(imp_result)), importance[imp_result], color='lightblue', align='center')
plt.xticks(range(len(imp_result)), feat_labels, rotation=90)
plt.xlim([-1, len(imp_result)])
plt.tight_layout()
plt.xticks(rotation=80)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()


dt = pd.DataFrame(train[a_labels])
#dt.to_csv("result3_csv.csv", index=0)

a_labels.append('j')
dt = pd.DataFrame(train[a_labels])
dt.to_csv("result4_csv.csv", index=0)

#train1= pd.read_csv('result_csvyuceliu.csv',encoding='GB2312')
#dt = pd.DataFrame(train1[a_labels1])
#dt.to_csv("result5_csv.csv", index=0)

#a_labels1.append('h')
#dt = pd.DataFrame(train1[a_labels1])
#dt.to_csv("result6_csv.csv", index=0)