class Person(object):
    name = ''
    age = ''
    gender = ''
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def roll_dice(self):
    	import random
        dices = [(j, i) for i in range(1, 7) for j in range(1, 7)]
        random.shuffle(dices)
        return dices[0]

