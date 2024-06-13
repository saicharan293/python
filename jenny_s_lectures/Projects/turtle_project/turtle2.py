from turtle import Turtle,Screen
s1=Screen()
t=Turtle()
# t.title('Python turtle part 2')
t.shape('turtle')
t.width(4)
# t.pencolor('red')
t.color('red','green')
t.begin_fill()
t.circle(100)
t.end_fill()

#pencolor=> outer side only
# t.pencolor('red')

#color=> total space
# t.color('red')

#fillcolor=> inner space only
# t.fillcolor('green')
# t.screen.mainloop()
s1.exitonclick()
