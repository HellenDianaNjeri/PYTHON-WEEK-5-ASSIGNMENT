# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!)
class Superhero:
    def __init__(self, name, power, eye_color, strength_level):
        self.name = name
        self.power = power
        self.eye_color = eye_color
        self.strength_level = strength_level  # 1 to 100

    def introduce(self):
        return f"I am {self.name}, my power is {self.power}!"

    def power_boost(self, boost):
        self.strength_level += boost
        return f"{self.name}'s strength increased to {self.strength_level}!"

    def get_stats(self):
        return {
            "Name": self.name,
            "Power": self.power,
            "Eye Color": self.eye_color,
            "Strength": self.strength_level
        }

# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, eye_color, strength_level, flight_speed):
        super().__init__(name, power, eye_color, strength_level)
        self.flight_speed = flight_speed  # in km/h

    def introduce(self):  # Polymorphism: method overridden
        return f"I am {self.name}, and I fly at {self.flight_speed} km/h!"

    def fly(self):
        return f"{self.name} takes off into the skies!"

# encapsulation_example = Superhero("Invisible"
class StealthSuperhero(Superhero):
    def __init__(self, name, power, eye_color, strength_level):
        super().__init__(name, power, eye_color, strength_level)
        self.__invisibility_level = 0  # Private attribute

    def become_invisible(self):
        self.__invisibility_level = 100
        return f"{self.name} is now fully invisible!"

    def get_invisibility_status(self):
        return f"Invisibility Level: {self.__invisibility_level}"
