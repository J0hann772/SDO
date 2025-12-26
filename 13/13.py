
ip1 = [163,135,196,55]
ip2 = [163,135,210,181]

ip1_str = ''
ip2_str=''


for i in range(len(ip1)):
    ip1[i]=bin(ip1[i])[2:]
    ip1[i]='0'*(8-len(ip1[i]))+ip1[i]

ip1 = '.'.join(ip1)


for i in range(len(ip2)):
    ip2[i] = bin(ip2[i])[2:]
    ip2[i] = '0' * (8 - len(ip2[i]))+ip2[i]

ip2 = '.'.join(ip2)

"""
10100011.10000111.110 00100.00110111
10100011.10000111.110 10010.10110101
                     ^
19 символов маска, 10 единиц в маске
"""

print('10100011.10000111.110_00000.00000000'.count('1'))
c=0
for i in range(2**13):
    if bin(i)[2:].count('1') == 11:
        c+=1

print(c)

