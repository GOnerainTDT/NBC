import numpy as np
import csv
import Species_class

def read_csv(filename):
    iris = []
    with open(filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            temp_Iris = Species_class.Species(row[0].replace('\ufeff', ''), row[1], row[2], row[3], row[4])
            print(row)
            iris.append(temp_Iris)
    return iris

#感知器算法
def perceptron(w, x, y):
    w = np.reshape(w, (5, 1))
    wT = np.reshape(w, (1, 5))
    x = np.reshape(x, (5, 1))
    print('w: ', w)
    print(y, ' * ', np.dot(wT, x), ' = ', y * np.dot(wT, x))
    if y * np.dot(wT, x) <= 0:
        print('before: ', w)
        w = w + 0.005 * y * x
        print('after: ', w)
    return w

iris = read_csv('temp/22.csv')
w1, w2,w3, w4, w0 = 1,1,-1,-1,0
w = np.array([w1, w2, w3, w4, w0])

for i in range(6):
    for row in iris:
        x = np.array([float(row.sepal_length), float(row.sepal_width), float(row.petal_length), float(row.petal_width), 1])
        if row.species == 'Iris-setosa':
            y = 1
        else:
            y = -1
        x.astype(float)
        w.astype(float)
        print("num: ", i, " --------------")
        w = perceptron(w, x, y)
        print('----------------------')
    
print(w)

# 测试w
for i in range(6, 10):
    x = np.array([float(iris[i].sepal_length), float(iris[i].sepal_width), float(iris[i].petal_length), float(iris[i].petal_width), 1])
    print(x)
    x.astype(float)
    w.astype(float)
    print(np.dot(np.reshape(w, (1, 5)), x))