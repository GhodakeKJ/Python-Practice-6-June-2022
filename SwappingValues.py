a=int(input("Enter Of a  :"))
b=int(input("Enter Of b  :"))
print("Original Value Of a :",a)
print("Original Value Of b :",b)
#Swapping Logic
a=a^b
b=a^b
a=a^b
print("Swapping Value Of a:",a)
print("Swapping Value Of b:",b)