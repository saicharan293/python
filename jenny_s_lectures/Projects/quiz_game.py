import random

print('*' * 20)
print("Welcome to the Quiz game !!! ")
qn_bank = [
    {'text': "The ability of one class to acquire methods from another class is called? ",
     'answer': "A"},
    {'text': "Which of the following is a type of inheritance? ",
     'answer': "D"},
    {'text': "What type of inheritance has multiple subclasses to a single superclass? ",
     'answer': "C"},
    {'text': "What is the depth of multi-level inheritance? ",
     'answer': "C"},
    {'text': "What does the MRO stands for? ",
     'answer': "B"},
    {'text': "What is the term used to describe a class that cannot be instantiated? ",
     'answer': "A"},
    {'text': "Which concept allows a derived class to be treated as a base class type? ",
     'answer': "B"},
    {'text': "What type of inheritance involves a class being derived from more than one base class? ",
     'answer': "C"},
    {'text': "Which keyword is used to inherit a class in Python? ",
     'answer': "A"},
    {'text': "What is the output of the MRO in Python? ",
     'answer': "D"}
]


options = [
    ["A. Inheritance", 'B. Abstraction', 'C. Polymorphism', 'D. Object'],
    ['A. Single', 'B. Double', 'C. Multiple', 'D. both A and C'],
    ['A. Multiple inheritance', 'B. Multi-level inheritance', 'C. Hierarchical inheritance', 'D. None of these'],
    ['A. Two level', 'B. Three level', 'C. Any level', 'D. None of these'],
    ['A. Method Recursive Object', 'B. Method Resolution Order', 'C. Main Resolution Order', 'D. Method Resolution Object'],
    ['A. Abstract class', 'B. Concrete class', 'C. Derived class', 'D. None of these'],
    ['A. Encapsulation', 'B. Polymorphism', 'C. Abstraction', 'D. Inheritance'],
    ['A. Single inheritance', 'B. Multi-level inheritance', 'C. Multiple inheritance', 'D. Hierarchical inheritance'],
    ['A. class', 'B. inherit', 'C. extends', 'D. derive'],
    ['A. A list of attributes', 'B. A dictionary of methods', 'C. A set of constructors', 'D. A linearization of the class hierarchy']
]


score=0
def check_answer(user,answer):
    return user==answer
qn_length=len(qn_bank)
for qn_no in range(qn_length):
    print('-'*50)
    print(qn_bank[qn_no]['text'])
    for i in options[qn_no]:
        print(i)
    user=input('Enter your answer (A/B/C/D): ').upper()
    is_correct=check_answer(user,qn_bank[qn_no]['answer'])
    if is_correct:
        score+=1
        print(f"Correct answer!!! ")
    else:
        print(f"Incorrect answer")
        print(f"The correct answer is", qn_bank[qn_no]['answer'])
    print(f"Your current score is {score}/{qn_no+1}")
print(f"You have given {score} correct answer")
print(f'Your final score is {int((score/qn_length)*100)}%')

