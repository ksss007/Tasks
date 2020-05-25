#!/usr/bin/env python3
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
s1 = input('Введите имя устройства: ')
s2 = london_co[s1]
s3 = list(s2.keys())
ss3 = str(s3).replace("[","(")
ss3 = ss3.replace(']',')')
s4 =("Введите имя параметра " + ss3 + ' : ')
s5 = input(s4)
s6 = london_co[s1][s5]
print (s6)