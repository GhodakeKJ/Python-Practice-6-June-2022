#Sequence data types
#str data type

a="Python is an oop language"
print(a,type(a),id(a)) #Python is an oop language <class 'str'> 17664825344

#single line comments
python="Guido van Rossum Launched The Python Language in Year 1991"
print(python,type(python)) #Guido van Rossum Launched The Python Language in Year 1991 <class 'str'>

#Multi line comments
Karan_information="""Name : Karan Jaywant Ghodake\n
Address:Bhose(k),tal:Pandharpur,Maharashtra\n
Course:Python\n
course2:Java\n
Course3:Android\n
Course4:UI"""
print(Karan_information)

''' Output
Name : Karan Jaywant Ghodake

Address:Bhose(k),tal:Pandharpur,Maharashtra

Course:Python

course2:Java

Course3:Android

Course4:UI'''
#indexing And Slicing On str

#syntax 1 (Index No)
k="PYTHON"
print(k[0])  # P
#print(k[99])  IndexError: string index out of range
print(k[5]) # N

#syntax 2 (start,stop)

print(k[0:6])  #PYTHON
print(k[4:77])  #ON

#syntax 3 (start:)

print(k[0:])  #PYTHON
print(k[2:]) #THON

#syntax 4 (:stop)

print(k[:-6])  #
print(k[:4])  #PYTH

#syntax 4 (:)
print(k[::])  #PYTHON

#syntax 4 (start,stop,step)
print(k[0:10:1])  #PYTHON
print(k[2:6:2])  #TO