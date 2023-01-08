
import pickle

class Vehicle:
    def __init__(self,windows, color,engine):
        self.windows = windows
        self.color = color
        self.tires = 4
        self.engine = engine
        
    def show(self):
        print(f'The vehicle color is {self.color}, and it has {self.windows} windows, and {self.tires} tires, with a motor type {self.engine}')
        
    
car = Vehicle(4,"black", "disel")
# car.show()
f = open('BinaryFile.bin', 'wb')
pickle.dump(car, f)
f.close()


# READ

t = open('BinaryFile.bin', 'rb')
car = pickle.load(t)
t.close()