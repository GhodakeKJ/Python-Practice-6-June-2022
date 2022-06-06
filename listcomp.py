print("Enter List Of Values Seperated by Space For Sum And Average :")
lst=[int(val)for val in input().split()]
print("Given List Elements :{}".format(lst))
s=0
for val in lst:
    print("\t\t{}".format(val))
    s=s+val
else:
    print("Sum :{}".format(s))
    print("Average :{}".format(s/len(lst)))