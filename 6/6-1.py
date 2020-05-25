#Задание 6.1
#Список mac содержит MAC-адреса в формате XXXX:XXXX:XXXX. Однако, в оборудовании cisco MAC-адреса используются в формате XXXX.XXXX.XXXX.

#Создать скрипт, который преобразует MAC-адреса в формат cisco и добавляет их в новый список mac_cisco

#Ограничение: Все задания надо выполнять используя только пройденные темы.

#mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']


mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cis = []
for item in mac:
    # print(list(item))
    l_item = list(item)
    m_mac = []
    for el in l_item:
        a = el
        m_mac.append(a.replace(':', '.'))
    #print (m_mac)
    mac_cis.append(m_mac)
st_mac = []
for el_mac in mac_cis:
    st_mac.append(''.join(el_mac))
print(st_mac)
