#int Data Type  Value without decimal point is 'int'data type
#Fundamental Data Types
a=123     #Here 'a' is Object
print(a)
print(a,type(a))  #123 <class 'int'>
print(a,type(a),id(a))  #123 <class 'int'> 140720344261472

x=453
y=53
z=x*y
print("Division :",z,type(z),id(z))  #Division : 24009 <class 'int'> 665022551024

#float Data Type  Value with decimal point is 'float'data type
print("="*80)
f=123.66
print(f,type(f),id(f))

k=123.6     #float Value
r=7656   #int Value
n=k+r
print(n,type(n),id(n))   #7779.6 <class 'float'> 928976777720  float output

#bool data type
print("="*80)
b=True
c=False
print(b,type(b),id(b)) #True <class 'bool'> 140720343726416
print(c,type(c),id(c))


#complex data type
print("="*80)
c1=4+3j
print(c1,type(c1),id(c1))
d1=+4j
print(d1,type(d1).imag)  #4j <member 'imag' of 'complex' objects>

e=55+7j
print(e,type(e).real)  #(55+7j) <member 'real' of 'complex' objects>

