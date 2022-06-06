big=lambda a,b,c:"All Values Are Same" if (a==b==c) else a if(b<=a>c) else b if(a<=b>c) else c

result=big(int(input("Enter First Value :")),int(input("Enter Second Value :")),int(input("Enter Third Value :")))
print("Result  :",result)