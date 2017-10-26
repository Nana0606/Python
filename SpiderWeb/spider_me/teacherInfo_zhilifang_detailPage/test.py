s = "abd"

#若s1.find(s2)的结果不在s2中，则返回-1
if s.find("cdsv") == -1:
  print("No 'is' here!")
else:
  print("Found 'is' in the string.")

a = {}
a['你好'] = "niao"
a['你好吗'] = "nihaoma"

b = {}
b['dada'] = "打啊打"
b['test'] = "测试"

result = dict(a, **b)
print(result)

ShuMu = ['9篇', '5篇', '2篇', '1篇']
JiGou = ['华东师范大学', '复旦大学', '上海电力学院', '首都师范大学']
node_PianShuPerJiGou = ""
for time in range(0, len(ShuMu)):
  node_PianShuPerJiGou = node_PianShuPerJiGou + JiGou[time] + ":" + ShuMu[time] + ";"
print(node_PianShuPerJiGou)
