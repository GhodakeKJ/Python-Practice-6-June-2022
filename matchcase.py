a=float(input("Enter Value For a  :"))
b=float(input("Enter Value For b  :"))

print("="*50)
print("\tArithmatic Operatores")
print("="*50)
print("\t1.Addition :{} and {} ={}".format(a,b,a+b))
print("\t2.Subtraction :{} and {} ={}".format(a,b,a-b))
print("\t3.Division :{} and {} ={}".format(a,b,a/b))
print("\t4.Multiplication :{} and {} ={}".format(a,b,a*b))
print("\t5.Modulo Div :{} and {} ={}".format(a,b,a//b))
print("\t6.Exponantion :{} and {} ={}".format(a,b,a**b))
print("\t7.Reaminder :{} and {} ={}".format(a,b,a%b))
print("="*50)
ch=int(input("Enter Your Choice :"))
match(ch):