import random

class Human:
    def __init__(self, age, name = "human", job = False, car = False):
        self.name = name
        self.age = age
        self.job = job
        self.car = car
        self.money = 0
        self.happiness = 50
        self.satiety = 50
        self.hydration = 50
    
    def eat(self, food):
        add = 0
        if food == "apple":
            add += 10
        elif food == "pizza":
            add += 25
        else:
            add += 18
        
        self.__up(add, "satiety")
    
    def drink(self, drink):
        add = 0

        if drink == "water":
            add += 40
        elif drink == "cola":
            add += 25
        else:
            add += 18
        self.__up(add, "hydration")

    def relax(self, time):
        add = time / 500 * random.randint(1, 4) * 1.11
        self.__up(add, "happiness")

    def work(self, time):
        if self.job:
            add = time * random.randint(1, 5)
            self.__up(add, "money")

    def get_time_to_get_to_work(self):
        if self.car:
            return 60 * 5 * random.randint(2, 3)
        else:
            return 60 * 40

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Job: {self.job}")
        print(f"Car: {self.car}")
        print(f"Money: {self.money}")
        print(f"Happiness: {self.happiness}")
        print(f"Satiety: {self.satiety}")
        print(f"Hydration: {self.hydration}")

    def __up(self, add, attr):
        value = getattr(self, attr)
        value += add

        if attr != "money" and value > 100:
            value = 100

        setattr(self, attr, value)

oleg = Human(name = "Oleg", age = 18, job = True, car = True)
oleg.get_info()

time = 19000
time_to_get_to_work = oleg.get_time_to_get_to_work()
time_to_relax = 5000

oleg.eat("pizza")
oleg.eat("apple")

oleg.drink("water")
oleg.drink("cola")

oleg.work(19000 - time_to_relax - time_to_get_to_work)
relax_time = max(0, time_to_relax - time_to_get_to_work)
oleg.relax(relax_time)

oleg.get_info()