from dataclasses import dataclass

@dataclass(slots=True)
#internally creates __init__ and __repr__ internallly
class Project:

    #these are class scope attributes
    project_name:str
    payment:int
    client:str

    def notify(self):
        print(f"Notifying the client about the progress of the {self.project_name}")

# general class concept is down below:
# class Project:
#     def __init__(self,project_name,payment,client):
#         self.project_name=project_name
#         self.payment=payment
#         self.client=client
    
#     def __repr__(self) -> str:
#         return f"Project(name={repr(self.project_name)}, payment={repr(self.payment)}, client={repr(self.client)})"
    
class Employee:
    def __init__(self, name, age, salary, project):
        self.name=name
        self.age=age
        self.salary=salary
        self.project=project


p=Project('Django app',20000,'Global solutions')
e=Employee('sai',23,20000,p)
p.notify()
# print(e.project)
# print(repr(p))
