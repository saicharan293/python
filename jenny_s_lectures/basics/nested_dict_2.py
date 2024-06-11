student_data=[{
        'name':'ram',
        'roll':10,
        'age':20,
        'course':'python'
    },
    {
        'name':'mohan',
        'roll':20,
        'age':22,
        'course':'java'
    }
]
def add_student(name,roll,age,course):
    student_data.append({'name':name,'roll':roll,'age':age,'course':course})

student=add_student('shyam',22,18,'c#')
print(student_data[-1])