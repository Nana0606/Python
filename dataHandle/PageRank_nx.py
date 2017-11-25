import pymysql
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()  # 因为是相关人员，所以无向图便可以

# 连接数据库
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='demo_researchers_new',
    charset='utf8'
)

# 获取游标
cursor = conn.cursor()

# 查询数据
sql_related = "SELECT * from related_teachers"
cursor.execute(sql_related)
related_teacher = cursor.fetchall()   # 获取相关教师表的信息，智立方上没有相关人员的教师是不包含在内的
sql_teacher = "SELECT * from teacherinfo"
cursor.execute(sql_teacher)
teacherinfo = cursor.fetchall()  # 获取教师表的信息，为了将related_teachers表中不涉及的教师添加进去

# 将所有出现在related_teachers表中的节点信息和边信息都添加到G中
for row in related_teacher:
    teacher_id = row[1]
    relatedTeac_id = row[3]
    G.add_edge(teacher_id, relatedTeac_id)

# 有些节点出现在了teacherinfo中，但是没有出现在related_teachers中，这里将其添加进去
for teacher in teacherinfo:
    id = teacher[0]
    if (id in G.nodes()) == False: #如果id没有添加到G中
        print(id)
        G.add_node(id)
        print(id)
print(G.nodes())
print(G.edges())
print(G.number_of_nodes())
print(G.number_of_edges())

# 将图形画出
# layout = nx.spring_layout(G)
# nx.draw(G, pos=layout, with_labels=True, hold=False)
# for index in G.edges_iter(data=True):
#     print(index)   #输出所有边的节点关系和权重
# plt.show()

# 将每个节点及其pagerank值存储到数据库中
# for node, value in pr.items():
#     # insert_sql = "INSERT INTO centrality(id, degree, pageRank) VALUES ('%d', '%d', '%f')"
#     # print(node, " ", G.degree(node), " ", value*1000)
#     # data_insert = (node, G.degree(node), float(round(value*1000, 4)))  #数据归1000化
#     # cursor.execute(insert_sql % data_insert)
#     # conn.commit()

# 求PageRank值
pr = nx.pagerank(G, alpha=0.75)
# print('pageRank值为： \n', pr)
# 网络度中心性
Degree_Centrality = nx.degree_centrality(G)
# print('Degree_Centrality值为： \n', Degree_Centrality)
# 各个节点Closeness
Closeness_Centrality = nx.closeness_centrality(G)
# print('Closeness_Centrality值为： \n', Closeness_Centrality)
# 各个节点Betweenness
Betweenness_Centrality = nx.betweenness_centrality(G)
# print('Betweenness_Centrality值为： \n', Betweenness_Centrality)

for key in pr:
    # print(key, " ", pr[key])
    insert_sql = "INSERT INTO centrality(ID, degree, pageRank, degree_centrality, closeness_centrality, betweenness_centrality) VALUES ('%d', '%d','%f', '%f','%f', '%f')"
    data_insert = (key, G.degree(key), float(round(pr[key] * 1000, 4)), float(round(Degree_Centrality[key] * 1000, 4)),
                   float(round(Closeness_Centrality[key] * 1000, 4)), float(round(Betweenness_Centrality[key] * 1000, 4)))  # 数据归1000化
    cursor.execute(insert_sql % data_insert)
    conn.commit()

