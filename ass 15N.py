#dot.format()
#input=aman is good
#output=good is aman

s="aman is good"
print("{c} {b} {a}".format(a="aman",b="is",c="good"))






s="aman is good"
a=s.split()
for i in a[::-1]:
    print(i,end=" ")
    
    
#dot.format
#input=AABBCCCDDEEFGGHHIJJLKKLLLAABC
#output=ABCDEFGHIJKL
list="AABBBCCDDEFGGHHIJJKKLABCD"
x=[]
y=[]
for i in list:
    if i not in x:
        x.append(i)
for i in x:
    if list.count(i) > 1:
        y.append(i)
print(y)

#when a list we can find only [30,40]
lis=[10,20,30,[40,50,60],70,80,90]
print(lis[2],lis[3][0])