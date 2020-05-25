s1 = input('Введите IP-сети в формате: 10.1.1.0/24:  ')
print(s1)
s1 = s1.split('/')

s_ip = s1[0]
s_ip = s_ip.split('.')

#print(s_ip)
#print(type(s_ip))
s_mask = s1[1]
oct1, oct2, oct3, oct4 = s_ip

print(f'''
    IP address:
    {int(oct1):<8} {int(oct2):<8} {int(oct3):<8} {int(oct4):<8}
    {int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}
 ''')
s2 = s1[1]
#print(s2)
s3 = 32 - int(s2)
#print(s3)

s4_1 = '1' * int(s2)
s4_0 = '0' * int(s3)

s5 = s4_1 + s4_0
#print(s5)
oct1 = s5[0:8]
oct2 = s5[8:16]
oct3 = s5[16:24]
oct4 = s5[24:32]

print(f'''
    Mask:
    {int(oct1,2):<8} {int(oct2,2):<8} {int(oct3,2):<8} {int(oct4,2):<8}
    {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
''')
