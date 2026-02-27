student_name=input("Student Name:")
sub1=int(input("Subject 1:"))
sub2=int(input("Subject 2:"))
sub3=int(input("Subject 3:"))
if (sub1< 0 or sub1 > 100) or (sub2 < 0 or sub2 > 100) or (sub3 < 0 or sub3 > 100):
    print("Error: Marks must be between 0 and 100 only")
print(f"Name :{student_name}")
total=sub1+sub2+sub3
print(f"Total :{total}/300")
percentage=(total/300)*1002
print(f"Percentage: {percentage}%")

if(percentage >=75):
  print("Grade A")
elif(percentage >=60):
  print("Grade B")
elif(percentage >=40):
  print("Grade C")
else:
  print("Grade F")

