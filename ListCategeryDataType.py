#List Categeury Data Types

#List()
l=[10,20,30,40,50,6066,7044] #Empty List
l1=list() #Empty List
l.append("Karan")    #append() for adding elements in list at last position
print(l)
l1.append("Rossum")
print(l1,type(l1))
l1.insert(1,"Scott")
l1.insert(0,"John")  #insert() for adding elements in list depend on index
print(l1)
l1.remove("Scott")
l1.remove("John")  #remove() for Based on content
print(l1)

l.remove(10)  ##remove() for Based on content
l.remove(20)
print(l)

#l.pop(10)  #IndexError: pop index out of range
print(l)

l.pop()  #pop means removeing last elements in given list
print(l)
print("="*100)
x=[10,10,20,10,20,30,40,"Karan"]
y=x
print(y,type(y))  #deep copy  [10, 20, 30, 40, 'Karan'] <class 'list'>
x.count("Karan")
print(x)

x.reverse() #original [10, 10, 20, 10, 20, 30, 40, 'Karan']
print(x)  #reverse  ['Karan', 40, 30, 20, 10, 20, 10, 10]

#tuple data type
print("="*111)
t=(10,33,450,5600,"Karan","Django")
print(t,type(t))  # (10, 33, 450, 5600, 'Karan', 'Django') <class 'tuple'>

lst=[10,20,30,["Python","Django"]]
print(lst,type(lst))  #Nested List  [10, 20, 30, ['Python', 'Django']] <class 'list'>
print(lst[2])

matricx=[[10,20,30],[40,50,60],[70,80,90]]
for row in matricx:
    print(row)
'''Output
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
'''
for val in matricx[1]:
    print(val)
'''Output
40
50
60
'''