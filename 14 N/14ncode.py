s="rangerover is a beast"
a=s.split()
for i in a:
    print(i[::-1],end=" ")
    
    
s="rangerover is a beast"
a=s.split()
for i in a[::-1]:
    print(i,end=" ")
    
s="rangerover is a beast"
def reverse(string):
    if len(string)==0:
        return string
    else:
        return reverse(string[1:])+string[0]
    
print(reverse(s))
