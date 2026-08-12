# a student scrored marks in 3 subjects . 
# take the marks as input from the user and calculate the total marks, percentage and grade of the student.   

marks1=int(input("enter marks of sunbject 1 ="))
marks2=int(input("enter marks of sunbject 2 ="))
marks3=int(input("enter marks of sunbject 3 ="))
total_marks=marks1+marks2+marks3
percentage=(total_marks/300)*100
print(f"total marks = {total_marks}")
print(f"percentage = {percentage:.2f}")