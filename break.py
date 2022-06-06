'''s="INDIAN"
for ch in s:
    print("\t\t{}".format(ch))
for i in s:
    if(s=="A"):
        print("\t\t{}".format(i))
    else:
        print()'''

lst=[10,20,30,50,60,60,80,50]
for i in lst:
    if(i==50):
        break
    else:
        print("{}".format(i))
else:
    print("*"*50)