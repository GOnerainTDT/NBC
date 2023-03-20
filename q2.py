import numpy as np

# 初始化模型参数
w = np.array([1, 1, -1, -1, 0],dtype=np.float64)
lr = 0.005
max_iter = 500

train_X = np.array([[5.1, 3.5, 1.4, 0.2],
                    [4.4, 2.9, 1.4, 0.2],
                    [5.8, 4, 1.2, 0.2],
                    [7, 3.2, 4.7, 1.4],
                    [5.7, 2.8, 4.5, 1.3],
                    [4.9, 2.4, 3.3, 1]])

train_y = np.array([1, 1, 1, -1, -1, -1])

test_X = np.array([[4.6, 3.4, 1.4, 0.3],
                   [5.7, 4.4, 1.5, 0.4],
                   [6.3, 3.3, 4.7, 1.6],
                   [5, 2, 3.5, 1]])

test_y = np.array([1, 1, -1, -1])

def step_function(x):
    if x > 0:
        return 1
    else:
        return -1

# 训练模型
for i in range(max_iter):
    for j in range(len(train_X)):
        y_pred = step_function(np.dot(w[:-1], train_X[j]) + w[-1])

        loss_Partial = (train_y[j] - step_function(np.dot(w[:-1], train_X[j]) + w[-1])) ** 2
        w[:-1] += lr * (train_y[j] - y_pred) * train_X[j]
        w[-1] += lr * (train_y[j] - y_pred)
        print(train_X[j],train_y[j], y_pred)
        print('if_pregress ', (train_y[j] != y_pred),' after ',w, ' loss_Partial ',loss_Partial)
    
    loss = 0
    for j in range(len(train_X)):
        loss += (train_y[j] - step_function(np.dot(w[:-1], train_X[j]) + w[-1])) ** 2
    print(f'Epoch {i+1}: Loss = {loss}')
    if loss == 0:
        break
    

correct = 0
for i in range(len(test_X)):
    if step_function(np.dot(w[:-1], test_X[i]) + w[-1]) == test_y[i]:
        correct += 1
print(f'Test Accuracy: {correct / len(test_X)}')
print(f'w = {w}')
