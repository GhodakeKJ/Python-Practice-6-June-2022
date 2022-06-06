lst=["Python","Java","Django",10,20,30,40,50,60]
print("="*50)
for val in lst:
    if(val==40):
        break
    else:
        print("\t\t{}".format(val))
"""Output :
        Python
		Java
		Django
		10
		20
		30
"""