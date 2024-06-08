#public: outside the class and also within the class
#protected: within class and within derived class(child class/inherited class)
#private:Only within class
#Note: by default, everything is public and 
# protected => '_' (under_score) but not complete restriction(just for representation for futhur purpose)
# private => '__'(double under_Score) but using Name mangling(dir), can use private...



class Student:
    def __init__(self,name,rollno,age):
        self.name=name #public obviously
        self._rollno=rollno #protected since '_'
        self.__age=age #private since '__'
    def __display(self):
        print(f"Hi, this is {self.name} of {self.__age} years old from Student class with roll: {self._rollno}")
    
    def privateDisplay(self):
        self.__display()
class Branch(Student):
    pass
st=Student('sai',12,23)
#Name mangling => second method using dir(-object-name)
# print(dir(st)) this provides the way to show how to access the private variables
print(st._Student__age)
st._Student__display()
# st.privateDisplay() #easy method
br=Branch('charan',13,24)
# print(br.__age)

# print(br._rollno) #since protected, better to avoid manipulating it

