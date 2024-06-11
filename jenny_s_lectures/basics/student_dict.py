student_marks={
    'sai':92,
    'harry':67,
    'dimpy':56,
    'rahul':41,
    'charan':99,
    'prem':34
}
student_grades={}
#keys only
for stud in student_marks:
    marks=student_marks[stud]
    if marks>90:
        student_grades[stud]="A+"
    elif marks>80:
        student_grades[stud]="A"
    elif marks>70:
        student_grades[stud]="B+"
    elif marks>60:
        student_grades[stud]="B"
    elif marks>50:
        student_grades[stud]="C"
    elif marks>40:
        student_grades[stud]="D"
    else:
        student_grades[stud]="F"
print(student_grades)