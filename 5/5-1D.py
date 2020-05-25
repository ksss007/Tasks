london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}

s1 = input('Введите параметр: ')
s2 = london_co[s1]
#print(s2)
s3 = list(s2)
ss3 = str(s3)
print('Введите параметр', ss3, ':  ')
s4 = input()
s4 = s4.lower()
print(s4)
print(s2.get(s4, 'Такого параметра нет!'))

#print(london_co[s1][s4]