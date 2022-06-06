def show(sno,sname,cname,*details,crs="Python",cnt="India",**keyval):    #Keyword Variable Length Arguments
    print("\t Student Number :{}".format(sno))
    print("\t Student Name   :{}".format(sname))
    print("\t Collage Name   :{}".format(cname))
    print("Student Details :")
    for val in details:
        print("\t\t{}".format(val))
    print("\t Course Name    :{}".format(crs))
    print("\t Student Country:{}".format(cnt))
    print("Student Marks :")
    for k,v in keyval.items():
        print("\t{}\t\t{}".format(k,v))

#Main Program
show(100,"Karan Ghodake","MSSS",10,20,30,Marathi=88,Hindi=98,English=87)
print("========================================")
show(200,"Guido Rossum","RED Lab",40,50,60,Marathi=58,Hindi=48,English=77)
print("========================================")
show(300,"Danish Ritche","C Lab",70,80,90,Marathi=48,Hindi=88,English=67)