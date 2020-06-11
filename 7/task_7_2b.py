# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

file = argv[1]
with open(file, 'r') as f, open('config_sw1_cleared.txt', 'w') as tf:
    for line in f:

        if line.startswith(' ' + ignore[0]):
            continue
        if line.startswith(ignore[1]):
            continue
        if line.startswith(ignore[2]):
            continue
        else:
            tf.write(line)
