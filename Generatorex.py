def KRange(x,y):
    while(x<=y):
        yield x
        x=x+1

obj=KRange(10,20)
while(True):
    try:
        print(next(obj))
    except StopIteration:
        break
"""OutPut
10
11
12
13
14
15
16
17
18
19
20
"""