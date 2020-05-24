access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
trunk = 1
access = 1
dict_in = {'trunk': "Введите разрешенные VLANы:  ", 'access': "Введите номер VLAN:  "}
mod_int = input('Введите режим работы интерфейса (access/trunk):  ')
type_int = input('Введите тип и номер интерфейса:   ')
n_v_lan = input(dict_in[mod_int])
dict_tem = {'trunk': trunk_template, 'access': access_template}


print('\n'.join(dict_tem[mod_int]).format(n_v_lan))
