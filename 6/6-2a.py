

ip = input("Введите IP адрес:  ")
list_ip = ip.split('.')
list_ip_ver = []
for el in list_ip:
    if el.isdigit():
        list_ip_ver.append(el)
    elif el == '.':
        list_ip_ver.append(el)
else:
    print('Неправильный IP-адрес')


int_ip = []
for el in list_ip:
    el = int(el)
    int_ip.append(el)
print(int_ip)
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