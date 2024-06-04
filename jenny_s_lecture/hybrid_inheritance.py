# class A:
#     def display(self):
#         print('A class: display method')
#
# class B(A):
#     def display(self):
#         print('B class: display method')
#
# class C:
#     def show(self):
#         print('C class: show method')
#
# class D(B,C):
#     def display(self):
#         print('D class: display method')
#
# d1=D()
# d1.show()

class University:
    def __init__(self,university_name):
        self.university_name=university_name
    def showDetails(self):
        print(f"university name is: {self.university_name}")

class Course(University):
    def __init__(self,university_name,course_name):
        University.__init__(self,university_name)
        self.course_name=course_name
    def showDetails(self):
        print(f"University is: {self.university_name} and Course is : {self.course_name}")


class Branch(University):
    def __init__(self,university_name,branch_name):
        University.__init__(self,university_name)
        self.branch_name=branch_name
    def showDetails(self):
        print(f"University is: {self.university_name} branch is : {self.branch_name}")

class Student(Course,Branch):
    def __init__(self,university_name,branch_name,course_name,student_name):
        # University.__init__(self,university_name)
        Branch.__init__(self,university_name,branch_name)
        Course.__init__(self,university_name,course_name)
        self.student_name=student_name
    def showDetails(self):
        print(f"{self.student_name} is from "
              f"{self.university_name} under "
              f"{self.branch_name} has taken {self.course_name}")
class Faculty(Course,Branch):
    def __init__(self,university_name,branch_name,course_name,faculty_name):
        # University.__init__(self,university_name)
        Branch.__init__(self,university_name,branch_name)
        Course.__init__(self,university_name,course_name)
        self.faculty_name=faculty_name
    def showDetails(self):
        print(f"{self.faculty_name} is from "
              f"{self.university_name} under "
              f"{self.branch_name} teaches {self.course_name}")

student=Student('jntu','ece','stld','sai')
student.showDetails()