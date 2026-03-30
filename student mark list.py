student_name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

tamil = int(input("Enter marks for Tamil: "))
english = int(input("Enter marks for English: "))
maths = int(input("Enter marks for Maths: "))
science = int(input("Enter marks for Science: "))
sst = int(input("Enter marks for Social Science: "))

total=tamil+english+maths+science+sst
avg=total/5
 
print("------ Student Marklist ------")
print("Student Name: ",student_name)
print("Student roll number: ",roll_no)
print("Tamil     :", tamil)
print("English   :", english)
print("Maths     :", maths)
print("Science   :", science)
print("Social Science      :", sst)
print("-----------------------------")
print("Total     :", total)
print("Average   :", avg)
