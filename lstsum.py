lst=[10,20,30,40,50,60,70,80]
s=0
for val in lst:
    print("\t\t{}".format(val))
    s=s+val
else:
    print("Sum Of list :{}".format(s))
    print("Average Of List :{}".format(s/len(lst)))