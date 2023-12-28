import csv
with open("studentmarksrecord.csv","w",newline='') as f:
    w=csv.writer(f)
    w.writerow(["student_name","student_rollno","telugu marks","Maths_marks","English marks","Hindi_marks","Science_marks","Social_marks","Total_marks","Average_marks","Percentage","Result"])
    n=int(input("enter number of employee to entry details: "))
    for i in range(1,n+1):
        print(i," STUDENTS MARKS DEATILS ")
        stuname=input("enter name : ")
        sturollno=int(input("enter rollno :"))
        telugu=int(input("enter telugu marks: "))
        hindi=int(input("enter hindi marks :"))
        english=int(input("enter english marks : "))
        maths=int(input("enter maths marks :"))
        science=int(input("enter science marks :"))
        social=int(input("enter social marks:"))
        x=(maths+english+hindi+science+social)
        total=x
        y=x/6
        avg=y
        z=x/600*100
        per=z
        result="pass" if per>=35 else "fail"
    
        w.writerow([stuname,sturollno,maths,telugu,english,hindi,science,social,total,avg,per,result])
    print("total emp data written to csv file ")