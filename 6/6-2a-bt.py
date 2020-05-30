'''Задание 6.2a
Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:

состоит из 4 чисел разделенных точкой,
каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение: „Неправильный IP-адрес“

Ограничение: Все задания надо выполнять используя только пройденные темы.

Задание 6.2b
Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input("Введите IP адрес:  ")
password_correct = False
while not password_correct:
    list_ip = ip.split('.')
    list_ip_ver = []
    for el in list_ip:
        d = False
        for el in list_ip:
            if not el.isdigit():
                d = True
        if d == True:
            print('Неправильный IP-адрес. IP содержит неправильный символ.')
            ip = input("Введите правильный IP адрес:  ")
            break
        if el.isdigit():
            i = 0
            for el in list_ip:
                list_ip_ver.append(int(el))
                i += 1
        if len(list_ip_ver) != 4:
            print('Неправильный IP-адрес. IP должет содержать 4 числа.')
            ip = input("Введите правильный IP адрес:  ")
            break
        a = False
        for el in list_ip_ver:
            if el > 255:
                a = True

        if a == True:
            print('Неправильный IP-адрес. Каждое число в IP адресе не более 255')
            ip = input("Введите правильный IP адрес:  ")
            break
        else:
            password_correct = True
            break
password_correct = True
print("IP правильный", ip)
int_ip = []
for el in ip.split('.'):
    el = int(el)
    int_ip.append(el)
if 1 < int_ip[0] < 223:
    print('Тип IP адреса „unicast“ ')
elif 224 < int_ip[0] < 239:
    print('Тип IP адреса „multicast“ ')
elif int_ip[0] == 255:
    lb = []
    for item in int_ip:
        if item == 255:
            lb.append(item)
    if len(lb) == 4:
            print('Тип IP адреса „local broadcast“')
elif int_ip[0] == 0:
    lb = []
    for item in int_ip:
        if item == 0:
            lb.append(item)
    if len(lb) == 4:
            print('Тип IP адреса „unassigned“')
else:
    print('Тип IP адреса „unused“')
