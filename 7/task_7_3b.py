# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

file = argv[1]
m = []
m1 = []
m2 = []
with open(file, 'r') as f:
    for line in f:
        if line.startswith(' '):
            m = line.rstrip().split()
            m2.append(m)

        for i in m:
            if i.isdigit():
                m1.append(i)
                m1.sort()
    # print(m1)
    m2.pop(0)
    m3 = tuple(m2)
    m4 = sorted(m2)
    ind = m1.index('1000')
    # print(ind)
    m5 = m4.pop(ind)
    m4.append(m5)
s = input('Введите № Vlan :')
# print(m2)
# print(m4)
for ll in m4:
    # print(ll)

    if s == ll[0]:
        print(' '.join(ll))
    else:
        continue
