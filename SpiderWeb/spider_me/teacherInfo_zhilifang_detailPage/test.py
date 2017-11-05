s = "abd"

#若s1.find(s2)的结果不在s2中，则返回-1
if s.find("ab") == -1:
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

print("**************")
university = ["华东师范大学", "河海大学", "南通大学计算机科学与技术学院", "华东师范大学软件学院"]
tempJG = ["华东师范大学", "南通大学"]
for toadd_index in range(0, len(university)):
  for added_index in range(0, len(tempJG)):
    if university[toadd_index].find(tempJG[added_index]) != -1:  # 说明将要添加的机构名称不在已经添加的中
      break
    if added_index == (len(tempJG) - 1):
      tempJG.append(university[toadd_index])
print(tempJG)


charNmae = ['郝晓玲', '韩冬梅', '黄海量', '张勇', '王明佳', '王淞昕', '陈元忠', '王英林', '韩景倜', '李艳红']
print(len(charNmae))
