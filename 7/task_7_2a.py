# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

file = argv[1]
with open(file, 'r') as f:
    for line in f:
        if line.startswith('!'):
            continue
        if line.startswith('version'):
            continue
        if line.startswith(' ' + ignore[0]):
            continue
        if line.startswith(ignore[1]):
            continue
        if line.startswith(ignore[2]):
            continue
        else:
            print(line.rstrip())
