#Type Casting Techniques In Python

a=10
print(a,type(a)) #10 <class 'int'>

#int to float
b=float(a)
print(b,type(b))  #10.0 <class 'float'>

#int to bool

c=bool(a)
print(c,type(c)) #True <class 'bool'>

#int to complex

d=complex(a)
print(d,type(d))  #(10+0j) <class 'complex'>

#int to str
d1=str(a)
print(d1,type(d1)) #10 <class 'str'>

print("="*80)
b=245.77
print(b,type(b)) #245.77 <class 'float'>

#float to int
e=int(b)
print(e,type(e))  #245 <class 'int'>

#float to bool

f=bool(b)
print(f,type(f))  #True <class 'bool'>

#float to complex
g=complex(b)
print(g,type(g))   #(245.77+0j) <class 'complex'>

#float to str

h=str(b)
print(h,type(h))  #245.77 <class 'str'>