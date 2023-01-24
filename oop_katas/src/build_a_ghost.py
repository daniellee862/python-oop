class Ghost:

    def __init__(self, name: str, speed: int, colour: str):
           self.name = name
           self.speed = speed
           self.colour = colour
           self.is_scared = False
      

    def can_be_eaten(self):
        return self.is_scared
    
    def frighten(self):
            self.is_scared = True 
            self.colour = 'blue'
    
    def speed_up(self):
           self.speed = round((self.speed * 1.1),2)
           return self.speed
      

class Blinky(Ghost):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed, colour)

class Pinky(Ghost):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed, colour)

class Inky(Ghost):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed, colour)

class Clyde(Ghost):
    def __init__(self, name, speed, colour):
        super().__init__(name, speed, colour)







            
