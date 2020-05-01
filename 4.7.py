mac = "AAAA.BBBB.CCCC"
mac_l = mac.split('.')
print (mac_l)
oct1,oct2,oct3 = mac_l
oct1 = int(oct1, 16)
oct2 = int(oct2, 16)
oct3 = int(oct3, 16)
b1 = bin(oct1)
b2 = bin(oct2)
b3 = bin(oct3)
print(f'''
    MAC Addres:
    {b1} {b2} {b3}''')
