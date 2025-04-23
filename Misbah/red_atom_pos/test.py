class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
        
        
    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.y)


class Person:
    def __init__(self, name):
        self.name = name
    
    
    def talk(self):
        print(f"I am {self.name}")
        
person1 = Person("John")
person1.talk()


person2 = Person("Bob")
person2.talk()




    
