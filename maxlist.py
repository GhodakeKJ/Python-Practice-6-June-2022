maxnum=lambda obj:max(lst)
minnum=lambda obj:min(lst)

print("Enter List Of Values Seperated By Space :")
lst=[float(val)for val in input().split()]
maximumnum=maxnum(lst)
minimumnum=minnum(lst)
print("Given List Of Elements :",lst)
print("Maximum Number In List :",maximumnum)
print("Minimum Number In List :",minimumnum)