# python3
# -*- coding: utf-8 -*-
# @Author  : lina
# @Time    : 2018/2/7 19:43
import numpy as np
import random

iterator_count = 0

def euclDistance(vector, matrix):
    distSquare = pow(matrix - vector, 2)  # 计算平方误差
    #  计算每一个样本各属性的平方和, axis=0表示将每个向量的第一个元素相加，axis=1表示将每个向量的所有元素相加
    distSquare_sum = distSquare.sum(axis=1)
    distances = pow(distSquare_sum, 0.5)
    return distances   # 返回的是一个列向量

# 中心点矩阵的初始化
def initCentroids(data, k):
    n = data.shape[1]   # 计算样本的维度
    m = data.shape[0]   # 计算样本个数
    centroids = np.zeros((k, n))    # 初始化中心点矩阵
    new_centroids = np.zeros((k, n))
    new_count = np.ones((k, n))   # 这边初始化为1，是因为偷懒了，因为若不初始化为1，后期有的center没有一个样本，此时除以样本个数0会抛出异常
    for i in range(0, k):
        ranVal = int(random.uniform(0, m))  # 在[0, m)之间取值
        centroids[i, :] = data[ranVal, :]
    return centroids, new_centroids, new_count

def kMeans(data, centroids, new_centroids, new_count):
    global iterator_count
    m = data.shape[0]  # 计算样本个数
    for i in range(0, m):
        current = data[i]   # 当前样本
        distances = euclDistance(current, centroids)   # 欧式距离
        index = distances.argsort()[0]  # 此节点对应的最小距离的中心点
        new_centroids[index, :] += current   # 将当前节点累加到对应的中心点上，便于后续求新的中心点
        new_count[index, :] += 1    # 计算每个中心点包含的样本数
    centroids = new_centroids / new_count   # 新的中心点
    iterator_count += 1
    if iterator_count <= 20:   # 设置迭代次数
        kMeans(data, centroids, new_centroids, new_count)
    return centroids



if __name__ == "__main__":
    """
    data: 每一个样本是一个行向量，其中维度分别表示语文、数学和外语的得分等级，data中包含4个样本，5*3维的矩阵
    labels: 表示data中每个样本对应的标签，5*1维的向量
    test_data： 测试样本
    """
    data = np.array([
        [1.658985, 4.285136],
        [-3.453687, 3.424321],
        [4.838138, -1.151539],
        [-5.379713, -3.362104],
        [0.972564, 2.924086],
        [-3.567919, 1.531611],
        [0.450614, -3.302219],
        [-3.487105, -1.724432],
        [2.668759, 1.594842],
        [-3.156485, 3.191137],
        [3.165506, -3.999838],
        [-2.786837, -3.099354],
        [4.208187, 2.984927],
        [-2.123337, 2.943366],
        [0.704199, -0.479481],
        [-0.392370, -3.963704],
        [2.831667, 1.574018],
        [-0.790153, 3.343144],
        [2.943496, -3.357075],
        [-3.195883, -2.283926]
    ])
    centroids, new_centroids, new_count = initCentroids(data, 3)
    centroids = kMeans(data, centroids, new_centroids, new_count)
    print(centroids)

