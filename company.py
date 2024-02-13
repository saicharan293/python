
# purely meant for object creation with no inheritance
from employee import Employee

class Company:
    def __init__(self):
        self.employees=[]
    
    def add_employee(self,new_emp):
        self.employees.append(new_emp)
    
    def display_employee(self):
        print("current employees are : ")
        for employee in self.employees:
            print(employee.fname,employee.lname)

def main():
    my_company=Company()

    emp1=Employee('sai','charan',20000)
    my_company.add_employee(emp1)

    emp2=Employee('ravi','karuva',24000)
    my_company.add_employee(emp2)

    emp3=Employee('mano','paga',18000)
    my_company.add_employee(emp3)

    my_company.display_employee()

main()