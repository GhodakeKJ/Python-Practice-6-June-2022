#DictDataType

dict={10:'karan',20:'Rossum',30:'Python'}
print(dict,type(dict),len(dict))  #{10: 'karan', 20: 'Rossum', 30: 'Python'} <class 'dict'> 3
dict.popitem()  #Removing last paire of key and value
print(dict)  #{10: 'karan', 20: 'Rossum'}

states={"TS":'HYD',"MH":'MUM',"KA":'BANG',"TN":'CHN'}
for k,v in states.items():
    print(k,"\t\t",v)
'''Output
TS 		 HYD
MH 		 MUM
KA 		 BANG
TN 		 CHN
'''

for st in states.keys():
    print(st)
'''Output
TS
MH
KA
TN
'''
for vl in states.values():
    print(vl)
'''Output
HYD
MUM
BANG
CHN
'''
for x in states:
    print(x)
'''Output
TS
MH
KA
TN
'''