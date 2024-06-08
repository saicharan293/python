#public: outside the class and also within the class
#protected: within class and within derived class(child class/inherited class)
#private:Only within class
#Note: by default, everything is public and 
#protected=> '_' (under_score) but not complete restriction(just for representation for futhur purpose)



class Student:
    def __init__(self,name,rollno):
        self.name=name #public obviously
        self._rollno=rollno #protected since '_'
    def display(self):
        print(f"Hi, this is {self.name} from Student class with roll:{self._rollno}")
class Branch(Student):
    pass
st=Student('sai',12)
# st.display()
br=Branch('charan',13)
# print(br._rollno) #since protected, better to avoid manipulating it

