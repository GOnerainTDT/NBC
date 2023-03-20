import numpy as np
import matplotlib.pyplot as plt

# 将四张图片拼接在一起
def plot_4pic(pic1, pic2, pic3, pic4):
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ax1.imshow(pic1)
    ax2.imshow(pic2)
    ax3.imshow(pic3)
    ax4.imshow(pic4)
    plt.show()
    plt.savefig('pic/4pic.png')

# 读取图片
def read_pic(filename):
    img = plt.imread(filename)
    return img

# 保存图片
def save_pic(pic, filename):
    plt.imsave(filename, pic)

# pic1 = read_pic('pic/setosa_sepal_length.png')
# pic2 = read_pic('pic/setosa_sepal_width.png')
# pic3 = read_pic('pic/setosa_petal_length.png')
# pic4 = read_pic('pic/setosa_petal_width.png')

# pic1 = read_pic('pic/versicolor_sepal_length.png')
# pic2 = read_pic('pic/versicolor_sepal_width.png')
# pic3 = read_pic('pic/versicolor_petal_length.png')
# pic4 = read_pic('pic/versicolor_petal_width.png')

pic1 = read_pic('pic/virginica_sepal_length.png')
pic2 = read_pic('pic/virginica_sepal_width.png')
pic3 = read_pic('pic/virginica_petal_length.png')
pic4 = read_pic('pic/virginica_petal_width.png')
plot_4pic(pic1, pic2, pic3, pic4)

