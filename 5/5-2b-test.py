from sys import argv
s_ip = argv[1]
#s_mask = argv[2]
#s1 = input('Введите IP-сети в формате: 10.1.1.0/24:  ')
#print(s1)
#s1 = s1.split('/')

#s_ip = s1[0]
s_ip = s_ip.split('.')

# print(s_ip)
# print(type(s_ip))
#s_mask = s1[1]
oct1, oct2, oct3, oct4 = s_ip

print(f'''
    IP address:
    {int(oct1):<8} {int(oct2):<8} {int(oct3):<8} {int(oct4):<8}
    {int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}
 ''')