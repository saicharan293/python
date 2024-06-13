from turtle import *

# getscreen()
color('blue')
# fillcolor('green')
width(3)
#triangle shape
# for step in range(3):
#     forward(100)
#     left(120)
# home()
begin_fill()

#circular form of shape:
# while True:
#     forward(230)
#     left(170)
#     if abs(pos()) < 1:
#         break


# spiral structure
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)

# rectangle
# for steps in range(1):
#     for c in ('red','yellow'):
#         color(c)
#         forward(150)
#         right(90)
#         forward(100)
#         right(90)

# pentagon
lt=['red','yellow','blue','white','green']
title('normal structure')
bgcolor('black')
speed(10)
for i in range(3):
    # fillcolor(lt[i])
    # begin_fill()
    print(lt[i])
    for _ in range(len(lt)):
        color(lt[_])
        forward(100)
        left(72)
    circle(50)
    # left(20)

    # end_fill()
    left(120)
right(5)  
forward(150)
right(80)
forward(200)
shape('turtle')
# hideturtle()
exitonclick()
# done()
# mainloop()