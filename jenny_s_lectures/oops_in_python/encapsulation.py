# wrapping of code into single unit
# Note: class consisting of attributes and methods related to a particular topic
# encapsulation: to hide the data from outside user, using access modifiers
# using getter and setter method to access private terms of encapsulation
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
        self.__age=age #private since '_ _'

    # using getters and setters
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if (age>18):
            print(f'Invalid age : {age},age should be less than 18')
        else:
            self.__age=age
    # def __display(self):
    #     print(f"Hi, this is {self.name} of {self.__age} years old from Student class with roll: {self._rollno}")
    
    # def privateDisplay(self):
    #     self.__display()
# class Branch(Student):
#     def show(self):
#         print(f'my roll is : {self.__age}')
st=Student('sai',12,18)
print(st.get_age())
st.set_age(17)
print(st.get_age())
# print(st._Student__age)
# br=Branch('charan',13,24)

