import numpy as np
import matplotlib.pyplot as plt
import csv
import Species_class

def read_csv(filename):
    iris = []
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            temp_Iris = Species_class.Species(row[0].replace('\ufeff', ''), row[1], row[2], row[3], row[4])
            iris.append(temp_Iris)
    return iris


iris = read_csv('temp/iris.csv')
setosa = iris[0:40]
versicolor = iris[50:90]
virginica = iris[100:140]
test_setosa = iris[40:50]
test_versicolor = iris[90:100]
test_virginica = iris[140:150]
test = test_setosa + test_versicolor + test_virginica

sepal_length = np.random.normal(size=40)
sepal_width = np.random.normal(size=40)
petal_length = np.random.normal(size=40)
petal_width = np.random.normal(size=40)
p_attribute = [[[], [], [], []], [[], [], [], []], [[], [], [], []]]
for i in range(3):
    if i == 0:
        data = setosa
        data_name = 'setosa'
    elif i == 1:
        data = versicolor
        data_name = 'versicolor'
    else:
        data = virginica
        data_name = 'virginica'
    for t in range(40):
        sepal_length[t] = float(data[t].sepal_length)
        sepal_width[t] = float(data[t].sepal_width)
        petal_length[t] = float(data[t].petal_length)
        petal_width[t] = float(data[t].petal_width)
    
    for t in range(4):
        if t == 0:
            data_attribute = sepal_length
            attribute_name = 'sepal_length'
        elif t == 1:
            data_attribute = sepal_width
            attribute_name = 'sepal_width'
        elif t == 2:
            data_attribute = petal_length
            attribute_name = 'petal_length'
        else:
            data_attribute = petal_width
            attribute_name = 'petal_width'

        # 确定区间范围
        bin_width = 0.2
        bins = np.arange(min(data_attribute), max(data_attribute) + bin_width, bin_width)

        # 计算直方图
        hist, bin_edges = np.histogram(data_attribute, bins=bins, density=False)

        # 绘制直方图并标注样本数量
        plt.bar(bin_edges[:-1], hist, width=bin_width, align='edge', alpha=0.5, edgecolor='black')
        for m in range(len(hist)):
            plt.text(bin_edges[m], hist[m], str(hist[m]), ha='center', va='bottom')
            print(bin_edges[i], hist[i])
        for n in range(30):
            binsit = int((test[n].get(t)-bin_edges[0])/bin_width)
            print('-------')
            print(min(data_attribute))
            print(max(data_attribute))
            print(test[n].__str__())
            print(t)
            if test[n].get(t) > min(data_attribute) and test[n].get(t) < max(data_attribute):
                p_attribute[i][t].append(float(hist[binsit])/40)
                print(p_attribute[i][t])
                print(i)
                print(binsit)
                print(hist[binsit])
                print('-------')
            else:
                p_attribute[i][t].append(0)
        print(p_attribute[i])
            

        plt.xlabel(attribute_name)
        plt.ylabel('Frequency')
        plt.title(data_name + ' - ' + attribute_name)
        plt.savefig('pic/'+ data_name + '_' + attribute_name + '.png')
        # plt.show()
        plt.clf()
p_pre = [[], [], []]
p_attribute = 0.1+np.array(p_attribute)
for i in range(30):
    if i < 30:
        p_pre[0].append(p_attribute[0][0][i]*p_attribute[0][1][i]*p_attribute[0][2][i]*p_attribute[0][3][i])
        p_pre[1].append(p_attribute[1][0][i]*p_attribute[1][1][i]*p_attribute[1][2][i]*p_attribute[1][3][i])
        p_pre[2].append(p_attribute[2][0][i]*p_attribute[2][1][i]*p_attribute[2][2][i]*p_attribute[2][3][i])
#写入csv文件
with open('temp/p_attribute.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['setosa_sepal_length', 'setosa_sepal_width', 'setosa_petal_length', 'setosa_petal_width',
                        'versicolor_sepal_length', 'versicolor_sepal_width', 'versicolor_petal_length', 'versicolor_petal_width',
                        'virginica_sepal_length', 'virginica_sepal_width', 'virginica_petal_length', 'virginica_petal_width'])
    for i in range(30):
        writer.writerow([p_attribute[0][0][i], p_attribute[0][1][i], p_attribute[0][2][i], p_attribute[0][3][i],
                         p_attribute[1][0][i], p_attribute[1][1][i], p_attribute[1][2][i], p_attribute[1][3][i],
                         p_attribute[2][0][i], p_attribute[2][1][i], p_attribute[2][2][i], p_attribute[2][3][i]])
        
with open('temp/p_pre.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['setosa', 'versicolor', 'virginica', 'pre_name', 'real_name'])
    for i in range(30):
        pre_name = ''
        real_name = ''
        if p_pre[0][i] > p_pre[1][i] and p_pre[0][i] > p_pre[2][i]:
            pre_name = 'setosa'
        elif p_pre[1][i] > p_pre[0][i] and p_pre[1][i] > p_pre[2][i]:
            pre_name = 'versicolor'
        else:
            pre_name = 'virginica'
        if i < 10:
            real_name = 'setosa'
        elif i < 20:
            real_name = 'versicolor'
        else:
            real_name = 'virginica'
        writer.writerow([p_pre[0][i], p_pre[1][i], p_pre[2][i], pre_name, real_name])

print('------------')
print(p_pre)
