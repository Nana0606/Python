import gc

if __name__ == "__main__":
    queryFile = open("xwbaxx_xlbs.txt", 'r', encoding='utf-8')
    urls = set()
    for query in queryFile:
        splitRes = query.split('\t')
        if len(splitRes) != 2:
            print(query, ' 格式不正确')
        else:
            name = query.split('\t')[0]
            university = query.split('\t')[1]
            data = name + university
            urls.add(data)
    print('不重复的数据总条数：', len(urls))
    del urls
    gc.collect()
