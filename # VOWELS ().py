# VOWELS ()
text="python is a not an easy untill we will practiced"
l=[char for char in text if char in "aeiou"]
print(len(l))
print(l)
print()

text="my enemies are always blessing me"
for char in text:
    if char.lower() in "aeiou" :
        print(char)

#square root of range from 1 to 20
l=[x*x for x in range(1,21)]
print(l)

# action with l1 and use l1 in l2
l1=[x*x for x in range(1,11)]
print(l1)
l2=[i for i in l1 if i%2==0]
print(l2)







