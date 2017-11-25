import numpy as np

a = np.array([
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 0]
], dtype=float)

def graphMove(a):  # 构造转移矩阵
    b = a.transpose()  # b为a的转置矩阵
    c = np.zeros(a.shape, dtype=float)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            c[i][j] = a[i][j] / (b[j].sum())  # sum()会求出每一行的所有元素之和
    print('c: \n', c)
    return c


def firstPr(c):  # pr值的初始化
    pr = np.zeros((c.shape[0], 1), dtype=float)  # 构造一个存放pr值的属性
    for i in range(c.shape[0]):
        pr[i] = float(1) / c.shape[0]
    print('pr: \n', pr)
    return pr


def pageRank(p, m, v):  # 计算PageRank的值
    # 注释的这种方法和下面没有注释的方法都是正确的，一个判断的是必须完全收敛，一个是满足一定的threshold即可
    # while ((v == p * np.dot(m, v) + (1 - p) * v).all() == False):  # 判断pr矩阵是否收敛,(v == p*dot(m,v) + (1-p)*v).all()判断前后的pr矩阵是否相等，若相等则停止循环
    #      print('v: \n', v)
    #      v = p * np.dot(m, v) + (1 - p) * v
    #      print('判断语句：', (v == p * np.dot(m, v) + (1 - p) * v).all())
    # return v
    v1 = np.array(v.shape, dtype=float)
    v1 = p * np.dot(m, v) + (1 - p) * v
    print('前面的v1： ', v1)
    while ( np.abs(v1 - v).all() > 0.00000001):
       v = v1
       v1 = p * np.dot(m, v) + (1 - p) * v
       print('v1_1: ', v1)
    return v1


if __name__ == "__main__":
    M = graphMove(a)
    pr = firstPr(M)
    p = 0.8 # 引入浏览当前网页的概率为p。假设p=0.8
    print('最终的值为： \n', pageRank(p, M, pr))
