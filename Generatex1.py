def Karan(x,y,z):
    while(x<=y):
        yield x
        x=x+z

obj=Karan(0,100,20)
while(True):
    try:
        print(next(obj))
    except StopIteration:
        break

'''OutPut
0
20
40
60
80
100
'''