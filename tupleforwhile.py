tpl=(10,20,40,50,60,70,33)

print("="*50)
print("By Using While Loop")
print("="*50)
i=1
while(i<len(tpl)):
    print("\t\t{}".format(tpl[i]))
    i=i+1
    print()
print("="*50)
print("By Using For Loop")
print("="*50)
for k in tpl:
    print("\t\t{}".format(k))