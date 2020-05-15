s1 = input('Введите IP-сети в формате: 10.1.1.0/24:  ')
print(s1)
s1 = s1.split('/')

s_ip = s1[0]
s_ip = s_ip.split('.')

# print(s_ip)
# print(type(s_ip))
s_mask = s1[1]
oct1, oct2, oct3, oct4 = s_ip

print(f'''
    IP address:
    {int(oct1):<8} {int(oct2):<8} {int(oct3):<8} {int(oct4):<8}
    {int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}
 ''')

s_ip_bin1 = str(bin(int(oct1)))
s_ip_bin1 = s_ip_bin1[2:]
l1 = 8 - len(s_ip_bin1)
s_ip_bin1 = '0' * l1 + s_ip_bin1
s_ip_bin2 = str(bin(int(oct2)))
s_ip_bin2 = s_ip_bin2[2:]
l2 = 8 - len(s_ip_bin2)
s_ip_bin2 = '0' * l2 + s_ip_bin2
s_ip_bin3 = str(bin(int(oct3)))
s_ip_bin3 = s_ip_bin3[2:]
l3 = 8 - len(s_ip_bin3)
s_ip_bin3 = '0' * l3 + s_ip_bin3
s_ip_bin4 = str(bin(int(oct4)))
s_ip_bin4 = s_ip_bin4[2:]
l4 = 8 - len(s_ip_bin4)
s_ip_bin4 = '0' * l4 + s_ip_bin4

s_ip_bin = s_ip_bin1 + s_ip_bin2 + s_ip_bin3 + s_ip_bin4
#print(s_ip_bin)
# s_ip_bin = bin(int(oct1))+bin(int(oct2))+bin(int(oct3))+bin(int(oct4))

# print(s_ip_bin1 + ' ' + s_ip_bin2 + ' ' + s_ip_bin3 + ' ' + s_ip_bin4)

s2 = s1[1]
# print(s2)
s3 = 32 - int(s2)
# print(s3)

s4_1 = '1' * int(s2)
s4_0 = '0' * int(s3)

s5 = s4_1 + s4_0
#print(s5)
oct1 = s5[0:8]
oct2 = s5[8:16]
oct3 = s5[16:24]
oct4 = s5[24:32]

poz0 = s5.find('0')
#print(poz0)
adr_net = s_ip_bin[0:poz0] + s5[poz0:]
#print(adr_net)
oct11 = adr_net[0:8]
oct22 = adr_net[8:16]
oct33 = adr_net[16:24]
oct44 = adr_net[24:32]

print(f'''
    Network:
    {int(oct11, 2):<8} {int(oct22, 2):<8} {int(oct33, 2):<8} {int(oct44, 2):<8}
    {oct11:<8} {oct22:<8} {oct33:<8} {oct44:<8}
''')

print("/", s_mask, f'''
    
    Mask:
    {int(oct1, 2):<8} {int(oct2, 2):<8} {int(oct3, 2):<8} {int(oct4, 2):<8}
    {oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
''')
