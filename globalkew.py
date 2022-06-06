a=10  #Global Variable
def fun1():
    global a
    a=a+1
def fun2():
    global a
    a=a*2

#main Program
print("Value Of a:{}".format(a))
fun1()
print("Value Of a In Fun1 :{}".format(a))
fun2()
print("Value Of a In Fun2 :{}".format(a))
