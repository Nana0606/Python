

dict = {
    ('冯建华', '清华大学'): 1,
    ('吴继兰', '上海财经大学'): 2,
    ('贾珈', '清华大学'): 3
}

for key in dict:
    print(key, " ", dict[key])

print('******************')
tea = ('冯建华', '清华大学')
name = '贾珈g '
university = '清华大学'

dict[(name, university)]=4

for key in dict:
    print(key[0], " ", dict[key])

print('******************')
print(dict.get((name, university)))
# print(dict.get('冯建华'))