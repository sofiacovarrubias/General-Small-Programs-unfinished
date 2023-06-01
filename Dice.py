import random

class Die:
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll_die(self, times = 1):
        rolls = []
        for i in range(1, times+1):
            roll = random.randint(1, self.num_sides)
            rolls.append(roll)

        print(f"Your rolls on a D{self.num_sides} are: {rolls}")


D6 = Die()
D10 = Die(num_sides=10)
D20 = Die(num_sides=20)

D6.roll_die(times=10)
D10.roll_die(times=10)
D20.roll_die(times=10)
