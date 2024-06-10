# Another alternative is explicit type checking, 
# where you check the type of an object before using it. 

class Bird:
    def fly(self):
        return 'Flap Flap!'

class Airplane:
    def fly(self):
        return 'Zoom Zoom!'

def in_the_sky(flier):
    #isinstance checks if flier is among the following items or not
    if isinstance(flier, (Bird, Airplane)):
        print(flier.fly())
    else:
        raise TypeError('The object does not know how to fly')

pigeon = Bird()
boeing = Airplane()
in_the_sky(pigeon)
in_the_sky(boeing)

#  In this example, the in_the_sky function checks whether the flier object is an instance of Bird or Airplane
#  before calling the fly method. If the object is not an instance of these classes,
#  the function raises a TypeError.