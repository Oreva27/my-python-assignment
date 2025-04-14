class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def show_identity(self):
        return f"I am {self.name} from {self.origin} and I have the power of {self.power}!"

class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.__flight_speed = flight_speed  # Encapsulated attribute

    def fly(self):
        return f"{self.name} flies at {self.__flight_speed} km/h!"

    def get_flight_speed(self):  # Encapsulation: Getter
        return self.__flight_speed
    
    # Test Run

# hero1 = Superhero("Shadow Flame", "Invisibility", "Unknown Realm")
# hero2 = FlyingHero("Sky Guardian", "Wind Control", "Sky City", 800)
# print(hero1.show_identity())
# print(hero2.show_identity())
# print(hero2.fly())

class Animal:
    def move(self):
        print("This animal moves in its own way...")

class Dog(Animal):
    def move(self):
        print("The dog runs and wags its tail.")

class Bird(Animal):
    def move(self):
        print("The bird flies through the sky.")

class Fish(Animal):
    def move(self):
        print("The fish swims in the water.")

        # Test it out
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()




