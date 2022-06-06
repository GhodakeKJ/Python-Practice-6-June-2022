n=int(input("Enter Any Number For Sum :"))
if(n<=0):
    print("{} Is Invalid Number Plz Enter +ve Number")
else:
    print("="*60)
    print("The Sum {} Given Number".format(n))
    s=0
    i=1
    while(i<=n):
        print("\t\t{}".format(i))
        s=s+i
        i=i+1
    else:
        print("Sum Of Given Nth Number Is : {}".format(s))