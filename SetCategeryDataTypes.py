#Set Categery Data Types

s={10,20,30,"Rossum","Django"}
print(s,type(s))  #{'Rossum', 10, 20, 'Django', 30} <class 'set'>
s.add("Travis")
s.add("English") #add() used for adding elements in list
print(s)  #{'Django', 'Travis', 10, 'English', 20, 'Rossum', 30}
s.clear()  #clear() is used for clear all elements in set
print(s)  #set()

s1={10,20,30,"Rossum","Django"}
s1.remove(10)  #remove() used for reveming special elements
print(s1)  #{'Rossum', 20, 'Django', 30}

s1.discard("Rossum")
print(s1)  #{'Django', 20, 30}

set1={10,20,30,40,50}
set2={40,50,60,70,80}
s3=set1.union(set2)  #union() used for selecting uniq values in sets
print(s3)  #{70, 40, 10, 80, 50, 20, 60, 30}
s4=set1.difference(set2)  #Specifing difference elements in set
print(s4)  #{10, 20, 30}

s5=set1.symmetric_difference(set2) #not showing common elements in set
print(s5)  #{80, 20, 70, 10, 60, 30}

s6=set1.intersection(set2)  ##showing common elements in set
print(s6) # {40, 50}

#frozenset data type
print("="*111)
fs={10,20,40,66,75,43,"Karan"}
fs1=frozenset(fs)
print(fs1,type(fs1))  #frozenset({66, 20, 40, 43, 10, 75, 'Karan'}) <class 'frozenset'>