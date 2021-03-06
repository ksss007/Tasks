# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

#ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
ignore = ['duplex', 'alias', 'Current configuration']

file_in = argv[1]
file_out = argv[2]
with open('file_in', 'r') as src, open('file_out', 'w') as dst:
    for line in src:

        if line.startswith(' ' + ignore[0]):
            continue
        if line.startswith(ignore[1]):
            continue
        if line.startswith(ignore[2]):
            continue
        else:
            dst.write(line)