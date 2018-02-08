# python3
# -*- coding: utf-8 -*-
# @Author  : lina
# @Time    : 2018/2/7 16:11
import numpy as np
import operator as opt


# 将矩阵规范化
def normData(data):
    min = data.min(axis=0)  # 求出每个属性的最小值
    max = data.max(axis=0)
    range = max - min
    norm_data = (data - min) / range
    return norm_data, min, range   # 返回数据，待函数使用，也应用于测试数据的规范化


def kNN(data, labels, test_data, k):
    distSquare = pow(data - test_data, 2)  # 计算平方误差
    #  计算每一个样本各属性的平方和, axis=0表示将每个向量的第一个元素相加，axis=1表示将每个向量的所有元素相加
    distSquare_sum = distSquare.sum(axis=1)
    distances = pow(distSquare_sum, 0.5)   # 开根号
    sort_dist_index = distances.argsort()   # 得到排序后的下标
    indexes = sort_dist_index[:k]   # 取距离最小的k个样本对应的下标
    labelCount = {}  # dict初始化
    for i in indexes:
        label = labels[i]    # 获得对应的label
        labelCount[label] = labelCount.get(label, 0) + 1   # 次数加1，get方法：dict.get(key, default=None)
    # 对label的次数从大到小排序， sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
    sortedCount = sorted(labelCount.items(), key=opt.itemgetter(1), reverse=True) #  After f = itemgetter(1), the call f(r) returns r[1].
    # sortedCount: [(1, 2), (0, 1)]   sortedCount[0]: (1, 2)
    return sortedCount[0][0]




if __name__ == "__main__":
    """
    data: 每一个样本是一个行向量，其中维度分别表示语文、数学和外语的得分等级，data中包含4个样本，5*3维的矩阵
    labels: 表示data中每个样本对应的标签，5*1维的向量
    test_data： 测试样本
    """
    data = np.array([
        [3, 4, 5],
        [7, 8, 10],
        [10, 8, 10],
        [8, 7, 7],
        [6, 2, 1]
    ])
    """
    a = array([1, 2]) 表示列向量 
    b = array([[1,2]]) 表示行向量 
    c = array([[1,2],[1,2]])表示一个2x2的矩阵 
    """
    labels = np.array([1, 1, 0, 1, 0])
    norm_data, min, range = normData(data)
    test_data = np.array([6, 9, 9])
    norm_test_data = (test_data - min) / range
    result = kNN(norm_data, labels, norm_test_data, 3)
    print(result)
