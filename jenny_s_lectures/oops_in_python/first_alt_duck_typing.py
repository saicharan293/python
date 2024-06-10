from abc import ABC, abstractmethod

class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bird(Flyer):
    def fly(self):
        return 'Flap Flap!'

class Airplane(Flyer):
    def fly(self):
        return 'Zoom Zoom!'

pigeon = Bird()
boeing = Airplane()
print(pigeon.fly())
print(boeing.fly())

# Output:
# 'Flap Flap!'
# 'Zoom Zoom!'
