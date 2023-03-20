import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# 读取数据集
data = pd.read_csv('temp/iris.csv', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# 将数据集中的类别用数字表示
data['class'] = pd.factorize(data['class'])[0]

# 划分训练集和测试集
train_data = pd.concat([data.iloc[:40,:], data.iloc[50:90,:], data.iloc[100:140,:]], axis=0).reset_index(drop=True)
test_data = pd.concat([data.iloc[40:50,:], data.iloc[90:100,:], data.iloc[140:150,:]], axis=0).reset_index(drop=True)

# 对每个特征进行直方图概率密度估计
train_data_hist = {}
for i in range(4):
    feature_name = data.columns[i]
    setosa = train_data[train_data['class']==0][feature_name]
    versicolor = train_data[train_data['class']==1][feature_name]
    virginica = train_data[train_data['class']==2][feature_name]
    bins = np.arange(data[feature_name].min()-0.5, data[feature_name].max()+0.5, 0.1)
    hist_setosa, _ = np.histogram(setosa, bins=bins, density=True)
    hist_versicolor, _ = np.histogram(versicolor, bins=bins, density=True)
    hist_virginica, _ = np.histogram(virginica, bins=bins, density=True)
    train_data_hist[feature_name] = {'setosa':hist_setosa, 'versicolor':hist_versicolor, 'virginica':hist_virginica}

# 基于朴素贝叶斯分类器进行分类
model = GaussianNB()
model.fit(train_data.iloc[:,:-1], train_data['class'])
train_data_pred = model.predict(train_data.iloc[:,:-1])
train_accuracy = accuracy_score(train_data['class'], train_data_pred)
test_data_pred = model.predict(test_data.iloc[:,:-1])
test_accuracy = accuracy_score(test_data['class'], test_data_pred)

# 计算分类错误的样本
train_data_errors = train_data[train_data['class']!=train_data_pred].index.tolist()
test_data_errors = test_data[test_data['class']!=test_data_pred].index.tolist()

# 输出分类准确率和分类错误的样本
print('Train Accuracy:', train_accuracy)
print('Train Errors:', train_data_errors)
print('Test Accuracy:', test_accuracy)
print('Test Errors:', test_data_errors)
