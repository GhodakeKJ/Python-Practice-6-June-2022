def show(sno,sname,cname,crs="Python",cnt="India"):    #KeyWord Variable Length
    print("\t Student Number :{}".format(sno))
    print("\t Student Name   :{}".format(sname))
    print("\t Collage Name   :{}".format(cname))
    print("\t Course Name    :{}".format(crs))
    print("\t Student Country:{}".format(cnt))

#Main Program
show(100,"Karan Ghodake","MSSS")
print("========================================")
show(200,"Guido Rossum","RED Lab")
print("========================================")
show(300,"Danish Ritche","C Lab")
print("========================================")
show(sno=400,crs="Django",cnt="USA",cname="LKG",sname="James Gosling") #KeyWord Variable Length