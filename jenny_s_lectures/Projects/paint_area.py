import math
def paint_calculation(ht,w,cover):
    area=ht*w
    cans_required=math.ceil(area/cover)
    print(f"you will need {cans_required} cans of paint")

ht=int(input("heigh of the wall in meters "))
w=int(input("width of the wall in meters "))
coverage=7
paint_calculation(ht,w,coverage)
