import pymysql
import pandas as pd

# 连接数据库
conn = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='demo_researchers_new',
    charset='utf8'
)

dict1 = {
    '冯建华': 1,
    '吴继兰': 2,
    '贾珈': 3,
    '金晶': 4,
    '陈岗': 5,
    '何高奇': 6,
    '刘知远': 7,
    '阮彤': 8,
    '韩松乔': 9,
    '李洪波': 10,
    '樊卫国': 11,
    '孙自强': 12,
    '李国良': 13,
    '冯佳昕': 14,
    '王淞昕': 15,
    '刘东林': 16,
    '邓俊辉': 17,
    '梁建宁': 18,
    '邓祖新': 19,
    '李进龙': 20,
    '高大启': 21,
    '史元春': 22,
    '朱小燕': 23,
    '范贵生': 24,
    '郭卫斌': 25,
    '向勇': 26,
    '李艳红': 27,
    '井然哲': 28,
    '余宏亮': 29,
    '王英林': 30,
}

dict2 = {
    ('冯建华', '清华大学'): 1,
    ('吴继兰', '上海财经大学'): 2,
    ('贾珈', '清华大学'): 3,
    ('金晶', '华东理工大学'): 4,
    ('陈岗', '上海财经大学'): 5,
    ('何高奇', '华东理工大学'): 6,
    ('刘知远', '清华大学'): 7,
    ('阮彤', '华东理工大学'): 8,
    ('韩松乔', '上海财经大学'): 9,
    ('李洪波', '清华大学'): 10,
    ('樊卫国', '上海财经大学'): 11,
    ('孙自强', '华东理工大学'): 12,
    ('李国良', '清华大学'): 13,
    ('冯佳昕', '上海财经大学'): 14,
    ('王淞昕', '上海财经大学'): 15,
    ('刘东林', '华东理工大学'): 16,
    ('邓俊辉', '清华大学'): 17,
    ('梁建宁', '华东理工大学'): 18,
    ('邓祖新', '上海财经大学'): 19,
    ('李进龙', '华东理工大学'): 20,
    ('高大启', '华东理工大学'): 21,
    ('史元春', '清华大学'): 22,
    ('朱小燕', '清华大学'): 23,
    ('范贵生', '华东理工大学'): 24,
    ('郭卫斌', '华东理工大学'): 25,
    ('向勇', '清华大学'): 26,
    ('李艳红', '上海财经大学'): 27,
    ('井然哲', '上海财经大学'): 28,
    ('余宏亮', '清华大学'): 29,
    ('王英林', '上海财经大学'): 30,
}


# 获取游标
cursor = conn.cursor()

# 查询数据
sql = "SELECT * from related_teachers"
cursor.execute(sql)
id = 31
for row in cursor.fetchall():
    # 有元素tuple0-ID、tuple1-教师编号、tuple2-教师姓名、tuple3-相关教师编号、tuple4-相关教师姓名、tuple5-相关教师学校、
    # tuple6-相关作品数、tuple7-相关教师作品数
    print(row)
    #print("tuple[0]: ", row[0], "tuple[1]: ", row[1])
    teacher_id = dict1.get(row[2])
    print('teacher_id is：', teacher_id)
    if dict2.get((row[4], row[5])):
        # 若不等于None，说明这个数据已经存在，则直接将数据插入
        relatedTeac_id = dict2.get((row[4], row[5]))
        # 更新相关教师表信息
        update_sql = "UPDATE related_teachers SET teacher_id = '%d', relatedTeac_id = '%s' WHERE ID = '%d'"
        data = (teacher_id, relatedTeac_id, row[0])
        cursor.execute(update_sql % data)
        conn.commit()
    else:
        # 若等于None，则数据不存在，则添加数据
        # 更新相关教师表信息
        update_sql_1 = "UPDATE related_teachers SET teacher_id = '%d', relatedTeac_id = '%d' WHERE ID = '%d'"
        data_update = (teacher_id, id, row[0])
        cursor.execute(update_sql_1 % data_update)
        # 向教师表信息中添加新信息
        insert_sql = "INSERT INTO teacherinfo(ID,teacher_chinese_name, university_name) VALUES ('%d', '%s', '%s')"
        data_insert = (id, row[4], row[5])
        cursor.execute(insert_sql % data_insert)
        conn.commit()
        # 更新dict2
        dict2[(row[4], row[5])] = id
        id = id + 1


