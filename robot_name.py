import string
import random
class Robot(object):

    def __init__(self):
        self.name = Robot.name()
   
    def name():
        name = ""
        for i in range(5):
            if i < 2:
                name += random.choice(string.ascii_uppercase)
            else:
                name += str(random.randrange(10))
        return name
   
    def reset(self):
        random.seed()
        self.name = Robot().name
        