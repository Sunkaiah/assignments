# difference between remove & pop & diacrd

# REMOVE ()
L1=[10,20,30,40,50,60]
L1.remove(60)
print(L1)

#2
s={10,20,30,40,50}
print("intial set : ",s)
s.remove(20)
print("updated set : ",s)

#3
l=[90,80,70,60,50]
for item in l.copy():
    if item > 100:
        l.remove(item)
    print(l)
    
#4
l=['sunku','pandu','hari','hema']
l.remove('hema')
print(l)

#5
numbers=[5,10,15,20,25,30]
for num in numbers:
    if num % 2==0:
        numbers.remove(num)
print(numbers)

#pop ()
fruits=['apple','grapes','banana','mango']
print("original : ",fruits)
fruits.pop(1)
print("after items are :",fruits)
fruits.pop(2)
print("after items are : ",fruits)

#2
student={'name':'sunku','age':23,'mail':'kammmarisunku048@gmail.com'}
student=student.pop('age')
print(student)
print(student)

#3
student={'name':'sunku','age':23,'mail':'kammmarisunku048@gmail.com'}
student=student.pop('name')
print(student)

#4
numbers=[2,4,6,8,10]
numbers.pop()

#DISCARD()
a={10,20,'sunku',30}
print('original set',a)
print(id(a))
print()
a.discard('hari')
print("after removing",a)
print(id(a))

#2
a={2,4,6,8}
a.discard(8)
print(a)

#3
a={'sunku','hari','hema','pandu'}
a.discard('hema')
print(a)

#4
l={200,300,400,500}
l.discard(600)
print(l)

#5
l={100,200,300,400,500}
l.add(700)
print(l)


#difference between the remove & pop & discard
# remove ()
1.remove the first item from the list whole value is mentioned 
2.return type is none 
3.it will modify the original list itsel.find()
4.it raises a values error if there is no such it item

# POP():
1.remove the item at a given position in the list and return it
2.it will return the element which is removed from the list
3.its also updated the original list and return the element
4.if index is not mentioned it removes and return the last element in the list

# write the pro to take tuple of numbers from key board and print sum avg
t=(10,20,30,40,50,60)
print(len(tuple))
avg=len(tuple)
sum=0
for i in tuple:
    sum=sum+i
print(sum)

# 
t=(20,40,60,80,70,)
sum=0
for i in t:
    sum=sum+i
print(sum)

#
t=(10,20,30,40,50,60)
sum=0
avg=len(t)
for i in t:
    sum=sum+i
print(sum/avg)









