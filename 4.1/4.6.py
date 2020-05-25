'''Задание 4.6
Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:

Protocol:               OSPF
Prefix:                 10.0.24.0/24
AD/Metric:              110/41
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
'''


ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.lstrip(ospf_route[0])
list = ospf_route.split()
list[1] = list[1].strip('[]')
list2 = ['Protocol: OSPF', 'Prefix:', 'AD/Metric:', 'Next-Hop:', 'Last update:', 'Outbound Interface:']
list[3]=list[3].rstrip(',')
list[4]=list[4].rstrip(',')
pf1,zn1,pf2,zn2,pf3,zn3,pf4,zn4,pf5,zn5 = [list2[1],list[0],list2[2],list[1],list2[3],list[3],list2[4],list[4],list2[5],list[5]]
print (f'''
        Protocol:                OSPF
        {pf1:<25}{zn1:<8}
        {pf2:<25}{zn2:<8}
        {pf3:<25}{zn3:<8}
        {pf4:<25}{zn4:<8}
        {pf5:<25}{zn5:<8}
        
        ''')