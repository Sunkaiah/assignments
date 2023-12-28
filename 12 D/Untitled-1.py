#functions : function is a structure is used to represent the busines logics to perform in the operations . 
#* function is not exuceted atomatically.
# function is called adress with which is prasent inside function name variable .
# example :
print("start")
def myfunc():
    print("welocome")
print(myfunc)
myvar=(myfunc)
print(myvar)
myfunc()
myfunc()
myvar()
print("end")
# default argument:
# parametrs: two types :
#1) non default parameters 2) default parameters

# non default parametrrs . 
# the parameters with decleare with out assing the values are non deafult para meters . 
# at the time of calling function compulasary pass the values. 
# example:
print("start")
def add(a,b):
    c=a+b
    print(c)
add(1000,2000)
add(10,20)
add(1234,5678)
print("close")

# default parameters.
#the parameters which declears by assing the values are knoen as a default parameters . 
print("start")
def add(a=10,b=20):
    c=a+b
    print(c)
add()
add(1000)
add(100,200)
print("end")
# example of defalt and non deafult.
def add(a,b=20):
    c=a+b
    print(c)
add(100,200)
add(123)

def aman():
    print("aman")
aman ()


def odd(x):
    if x%2!=0:
        print("odd")
    else:
        print("even")
odd(16)
odd(56)
odd(34)
odd(34)
odd(23)
odd(45)


def add(n):
    a=1
    while n>=1:
        a=a*n
        n=n-1
    return a
print(add(12))

def add(a,b):
    c=a+b


# key word argument:
#this ar'gument are passing by assigning to the parameter names is key word argument.
# important note*
#after passing the key word argument we are not allowed pass non key word argument  other wise are syntax error.

print()
def myfunc(name,msg):
    print("hello",name,msg)
myfunc(name="pandu",msg="good afternoon")
myfunc(msg="good afternoon",name="pandu")

#

print()
def ram(name,msg):
    print("hello",name,msg)
ram(name="hii sunkaiah achari",msg="good afternoon")
ram(msg="good afternoon",name="hi sunkaiah achari ")
ram(msg="hii ",name="aman")

#

print()
def myfunc(name,roll ):
    print("hello",roll ,name)
myfunc(name="hari",roll ="1234")
myfunc(roll="1234",name="hari")

#
print()
def myfunc(name,msg):
    print("welcome",name,msg)
myfunc(name="hello",msg="nagesh")
myfunc(msg="how are you",name="achari")





# positional argument:
# this argument which are passing directly with out assining the parameter names are known as positional argument.

print()
def func(name,msg):
    print("hello",name,msg)
func("aman","good afternoon")
func("good afternoon","aman")
print()

#
print()
def func(name,msg):
    print("hello",name,msg)
func("ram","how are you")
func("welocome ","sunku")
func("karthik","how are you")
func("how r you ","hari")

# variable  leangth arguments.
#in order to pass the different numbers of argument to a single parameter and we use variable length
# in oreder to declare to variable length arguments we use single * and multi** 

#pro to print sum if given number in var length.
def add(*a):
    s=0
    for p in a:
        s=s+p
    print(s)
add(10)
add(1000,2000)
add(10,20,30,40,50)
add(10+50)
# variable length argument.
def add(p,v,*a):
    print(p)
    print(v)
    print(a)
add(1000,2000)
add(10,20,30,40,50)


#
def add(*a,p,v):
    print(a)
    print(p)
    print(v)
add(10,20,30,p=40,v=50)
add(101,102,103,p=104,v=105)
#
def f(b,r,*a):
    print(b)
    print(r)
    print(a)
f(1000,2000,3000)
f(10,20,30,40,50)


# global variables.
# local variables

#global variables:
# global variables are pro can be acess with in all of functions of directly

a=1000
b=2000
def f1():
    print(a)
    print(b)
def f2():
    print(a)
    print(b)
f1()
f2()

# note:
# in order to modify the global variable data eith in the functions we use the global declaration.
a=1000
b=2000 
def f1():
    global a,b
    print(a)
    print(b)
    a=a+100
    b=b-100
def f2():
    print(a)
    print(b)
f1() 
f2()
# local variable:

def f1():
    a=1000 
    b=2000 
    print(a)
    print(b)
    a=a+100 
    b=b-100 
    print(a)
    print(b)
def f2():
    c=3000 
    d=4000 
    print(c)
    print(d)
    print(a)
    print(b)
f1()
f2()


