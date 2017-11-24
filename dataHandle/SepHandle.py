f = open('zhilian.txt', mode='r', encoding='utf-8')

# 处理memo字段，处理过的memo字段是去除分割符的字符串
while True:
    line = f.readline()
    if line:
        #print(line)
        strs = line.split(sep='\t')
        number = len(strs)
        memo = ''
        for i in range(13, number-3):
            memo = memo + strs[i]
    else:
        break
f.close()
