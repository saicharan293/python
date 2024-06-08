questions=[
    {
        'prompt':'what is the capital of India ?',
        'options':['A. Kolkata','B. Hyderabad','C. Delhi','D. JK'],
        'answer':'C'
    },
    {
        'prompt':'What is the language primarily spoken in India ?',
        'options':['A. English','B. Hindi','C. Telugu','D. Kannada'],
        'answer':'B'
    },
    {
        'prompt':'What is the smallest prime number ?',
        'options':['A. 1','B. 2','C. 3','D. 5'],
        'answer':'B'
    },
    {
        'prompt':'What does ANN stands for, in Deep Learning ?',
        'options':['A. Architectural Neural Networks','B. Authentic Neutral Networks','C. Authorized Neural Networks','D. Artificial Neural Networks'],
        'answer':'D'
    },
]
print('welcome to the quiz ')
def start(questions):
    score=0
    for q in questions:
        print(q['prompt'])
        for opt in q['options']:
            print(opt)
        print('answer is ',q['answer'])
        my_answer=input('Enter your answer: ').capitalize()
        if my_answer==q['answer']:
            score+=1
            print('Correct, go for next question ')
        else: 
            print('No, Answer is ',q['answer'])
    print(f'your scored {score} out of {len(questions)}')

start(questions=questions)


