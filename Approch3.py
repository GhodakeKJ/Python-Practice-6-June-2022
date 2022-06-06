def sumop():
    p=int(input("Enter First Value   :"))
    q=int(input("Enter Second Value  :"))
    r=p+q
    return p,q,r
a,b,result=sumop()
print("Sum :{} and {} ={}".format(a,b,result))