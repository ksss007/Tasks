# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from operator import itemgetter, attrgetter, methodcaller
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
    #print(m1)
    m2.pop(0)
    m3 = tuple(m2)
    m4 = sorted(m2)
    ind = m1.index('1000')
    #print(ind)
    m5 = m4.pop(ind)
    m4.append(m5)

    #print(m2)
    #print(m4)
for ll in m4:
    print(' '.join(ll))
