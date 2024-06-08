#Note: Diamond problem can be resolved using c3 linearisation
# using local precedence and monotonisation ,
# order starts from left to right, if not then go deep
class A:
    def display(self):
        print('A class: display function')

class B(A):
    def display(self):
        print('B class: display function')

class C(A):
    def show(self):
        print('C class: show function')
    def display(self):
        print('C class: display function')
class D(B,C):
    pass

d1=D()
d1.display()
print(D.mro())