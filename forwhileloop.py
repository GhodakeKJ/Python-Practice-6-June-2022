s="PYTHON"
print("="*50)
print("By Using For Loop")
print("="*50)
for i in s:
    print("\t\t",i)
print("="*50)
print("By Using While Loop")
print("="*50)
i=1
while(i<len(s)):
    print("\t\t{}".format(s[i]))
    i=i+1
