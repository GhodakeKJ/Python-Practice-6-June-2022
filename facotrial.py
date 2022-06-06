n=int(input("Enter Number For Finding Factorial :"))

if(n<=0):
    print("{} Is Invalid Number Plz Enter +ve Number For Factorial".format(n))
else:
    print("The Given {} Numbers".format(n))
    for i in range(1,n//2,+1):
        if(n%i==0):
            print("\t\t Factorials Are :{}".format(i))
