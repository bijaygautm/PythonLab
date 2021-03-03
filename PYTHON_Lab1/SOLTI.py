#A school decides to replace the desk in three classrooms. Each desk sits two students. Given the no of student in each
# class, print the smallest possible no of desk that can be purchased. The program should read three ints the no of stud
# in each three classes, a,b,c respectively.

lr13 = int(input("lr13 students:"))
lr14 = int(input("14 students:"))
lr15 = int(input("lr15 students:"))

totaldesk = round(lr13/2) + round(lr14/2) + round(lr15/2)
print(totaldesk)