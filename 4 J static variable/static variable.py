class studentdata():
    clg="svr engg college"
    def __init__(self,name,rollno,age):
        self.name=name
        self.rollno=rollno
        self.age=age
    def progress(self):
        print(self.clg,self.name,self.rollno,self.age)
a=studentdata("sunku",25,23)
a.progress()
studentdata("sunku",25,23).progress()
print()

#2 
# using class reference
class studentdata():
    clg="svr engg college"
    def __init__(self,name,rollno,age,section):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.section=section
    def progress(self):
        print(studentdata.clg,self.name,self.rollno,self.age,self.section)
a=studentdata("pandu",17,23,"B")
a.progress()
studentdata("sunku",25,23,"B").progress()
print()

class studentdata():
    clg="svr engg college"
    def record(self,name,rollno,age,section):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.section=section
    def progress(self):
        print(self.clg,self.name,self.rollno,self.age,self.section)
a=studentdata("sunku",25,23,"B")
a.record
a.progress()   #type error


#3
#using only constructor()
class studentdata():
    clg="chaitanya"
    def __init__(self,name,rollno,age,section):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.section=section
        print(self.clg,self.name,self.rollno,self.age,self.section)
        
a=studentdata("sunku",25,23,"B")
b=studentdata("pandu",17,22,"B")
c=studentdata("hari",19,23,"B")
d=studentdata("chandra",12,22,"B")
e=studentdata("jamal",20,23,"B")
print()

#4
# using 2 normal methods
class studentdata():
    clg="svr engg college"
    def record(self):
        name="sunku"
        age=23
        rollno=25
        section="B"
        print(studentdata.clg,name,rollno,age,section)
    def progress(self):
        name="jamal"
        age=23
        rollno=15
        section="B"
        print(studentdata.clg,name,rollno,age,section)
a=studentdata()
a.record()
a.progress()
print()

#5
# using print outside the method
class studentdata():
    clg="svr engg college"
    def record(self):
        name="sunku"
        age=23
        rollno=25
        section="B"
        print("hi")
    print(studentdata.clg,name,rollno,age,section)
a=studentdata()
a.record()
print() #nameerror:given variables are not defined


#6
# static variable print statement outside the method
class studentdata():
    clg="rgm engg college"
    def record(self):
        name="chandra"
        age=22
        rollno=12
        section="B"
        print("hi")
    print(studentdata.clg)
a=studentdata()
a.record()
print() 