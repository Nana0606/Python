
# 方法1：最基本的读文件的方法
file = open("in.txt", 'r', encoding='utf-8')

while True:
    line = file.readline()
    if not line:
        break
    print(line)

# 方法2：带缓存的文件读取，效率是第一种方法的3倍
file = open("in.txt", 'r', encoding='utf-8')

while 1:
    lines = file.readlines(2)
    if not lines:
        break
    for line in lines:
        print(line)

# 方法3：在python2.2之后，可以直接对一个file对象进行for循环读取每行数据
file =open("in.txt", 'r', encoding='utf-8')
for line in file:
    print(line)
