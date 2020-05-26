ip = input("Введите IP адрес:  ")
list_ip = ip.split('.')
print(list_ip)
int_ip = []
for el in list_ip:
    el = int(el)
    int_ip.append(el)
print(type(int_ip), int_ip)
