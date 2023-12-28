# EXTEND()
x=[1,2,3,4,]
y="567"
x.extend(y)
print(x)

#
x=[1,2,3,]
y="456"
x.extend(y)
print(y)

#
x=[1,2,3]
y={'x':7,'y':8,'z':9}
x.extend(y)
print(x)

#REMOVE()

l=[10,20,30,40,50]
for item in l.copy():
    if item<40:
        l.remove(item)
print(l)

#
s={20,30,40,50,60}
print("initial set : ", s)
s.remove(30)
print("updated set : ", s)


