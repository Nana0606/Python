import os
import networkx as nx
import matplotlib.pyplot as plt

# G = nx.Graph() # 创建一个空白图
# G = nx.DiGraph() # 创建一个空白有向图
#
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
#
# G.add_edge(1, 2, {'weight': 20})
# G.add_edge(1, 3, {'weight': 5})
# G.add_edge(2, 3, {'weight': 50})
# G[2][3]['weight'] = 100
#
# print(G.number_of_nodes()) # 所有节点的个数
# print(G.number_of_edges()) # 所有边的个数
# print(G.neighbors(3))  # 输出3节点的邻居节点，考虑有向的作用
# print(G.edges()) # 查找输出所有的边
# print(G[1][3])  # 访问权重
#
# for index in G.edges_iter(data=True):
#     print(index)   #输出所有边的节点关系和权重
#
# print(G.out_degree(1, weight='weight'))
# layout = nx.spring_layout(G)
# # node_size=[x * 6000 for x in G]
# nx.draw(G, pos=layout, with_labels=True)
# # plt.show()



H = nx.Graph() # 创建一个空白图

H.add_node(1)
H.add_node(2)
H.add_node(3)
H.add_node(4)

H.add_edge(1, 2, {'weight': 20})
H.add_edge(1, 3, {'weight': 5})
H.add_edge(2, 4, {'weight': 5})
H.add_edge(2, 3, {'weight': 5})
for index in H.edges_iter(data=True):
    print(index)   #输出所有边的节点关系和权重

print(H.degree(4))
print('***************************')

# layout = nx.spring_layout(H)
# # node_size=[x * 6000 for x in G]
# nx.draw(H, pos=layout, with_labels=True, hold=False)
# H.add_edge(3, 1, {'weight': 50})
# for index in H.edges_iter(data=True):
#     print(index)   #输出所有边的节点关系和权重
# plt.show()


dict = {1: 0.09486166007905138, 31: 0.001976284584980237, 32: 0.0009881422924901185, 33: 0.001976284584980237}
for key in dict:
    print(key, " ", dict[key])

array = [1, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print( (40 in array) == False)


array = ((1, '冯建华', 'Jianhua Feng', '清华大学', '教授', 'YOCSEF青年科学家', '惠普实验室创新研究奖'), (2, '吴继兰', 'Jilan Wu', '上海财经大学', '助理教授/讲师', None, None))
for arr in array:
    print(arr[0])



