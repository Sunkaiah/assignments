# 20 examples on functions

#1 adding 2 numbers using print
def add(num1,num2):
    print(num1+num2)
add(10,20)

#2 
def add(num1,num2):
    return num1+num2
x=add(10,20)
print(x)

#3
def number(n):
        print(n)
number(10)


#4 
def number():
    sum=0
    for i in range(1,21):
        if i%2==0:
            sum=sum+i
            i=i+1
    print(sum)
number()

#5 

def fac(n):
    a=1
    while n>=1:
        a=a*n
        n=n-1
    return a
print(fac(5))

#6 

def sq(n):
    print(n*n)
sq(5)

#7 

def rev(name):
    for i in name[::-1]:
        print(i,end=" ")
rev("sunku")
print()

#8 check if a string is a palindrome

name="pandu"
rname=name[::-1]
def pal():
    if name==rname:
        print("not a palindrome")
    else:
        print("palindrome")
pal()

#9 function with count
def count(name):
    a=name.count("a")
    b=name.count("e")
    c=name.count("i")
    d=name.count("o")
    e=name.count("u")
    list=[a,b,c,d,e]
    sum=0
    for i in list:
        sum=sum+i
    print("Number of vowels:",sum)
count("my name is sunkaiah achari and iam learning python programming language")

# 10  

def num(n):
    if n%2==0:
        print("even")
    else:print("odd")
num(11)

#11  

def even():
    l=[1,2,3,4,5,6,7,8,9,10]
    l1=[]
    for i in l:
        if i%2==0:
            l1.append(i)
    print(l1)
even()

#12  

l=[12,34,56,11,43,58,67]
def num():
    largest_number=max(l)
    l.remove(largest_number)
    second_largest=max(l)
    print(second_largest) 
num()

#13 

l=[1,2,3,45,1,34,23,3,89,56,34,3,1,2]
def num():
    a=set(l)
    b=list(a)
    print(b)
num()

#14 

l=[12,34,56,11,43,58,67]
def rev():
    l.reverse()
    print(l)
rev()

#15 function that accepts a sentence and returns the number of words in it

name="my name is sunkaiah achari and iam learning python programming language"
def words():
    a=name.count(" ")
    print(a+1)
words()

#16 

def average():
    l=[1,2,3,4,5,6]
    sum=0
    avg=len(l)
    for i in l:
        sum=sum+i
        i=i+1
    print(sum/avg)
average()