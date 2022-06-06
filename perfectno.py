n=int(input("Enter A Number :"))
if(n<=0):
    print("{} Is Invalid Number Plz Enter +ve Number")
else:
    s=0
    print("Given {} Is Number".format(n))
    for i in range(1,n//2):
        if(n%i==0):
            print("{}".format(i))


