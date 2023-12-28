n=int(input("enter number of students :"))
result={}
for i in range(n):
    print("enter details of student no.",i+1)
    rno=int(input("roll no:"))
    name=input("name: ")
    marks=int(input("marks: "))
    result[rno]=["name,marks"]
print(result)
for students in result:
    if result[student][1] > 75:
        print(result[student][0])