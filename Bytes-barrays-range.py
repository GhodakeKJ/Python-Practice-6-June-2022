#Bytes-barrays-range

#bytes data type
# b=[10,20,450,60,70]  ValueError: bytes must be in range(0, 256)
b=[10,20,255,60,70]
b1=bytes(b)
print(b1,type(b1))  #b'\n\x14\xff<F' <class 'bytes'>

print(b1[4]) #70
for i in b1:
    print(i)

'''Output
70
10
20
255
60
70
'''

#bytearray data type

ba=[10,20,30,50,60,70,44,255,33,54,64]
ba1=bytearray(ba)
print(ba1,type(ba1))  #bytearray(b'\n\x14\x1e2<F,\xff!6@') <class 'bytearray'>

for i in ba1[::-1]:
    print(i)

'''Output
64
54
33
255
44
70
60
50
30
20
10
'''
print("="*50)
for k in ba1[2:100:2]:
    print(k)

'''Output
30
60
44
33
64'''

#range data type
print("="*80)
for i in range(1,11):
    print(i)
'''Output
1
2
3
4
5
6
7
8
9
10'''
print("="*80)
for i in range(10,0,-1):
    print(i)
"""Output
10
9
8
7
6
5
4
3
2
1"""
print("="*80)
for i in range(-1,-11,-1):
    print(i,end="  ")
"""Outpu
-1  -2  -3  -4  -5  -6  -7  -8  -9  -10 
"""
print("="*80)
for i in range(-5,6,1):
    print(i,end="  ")
"""Output
-5  -4  -3  -2  -1  0  1  2  3  4  5  
"""