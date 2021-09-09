# David Martinez

# Write a program to show how multilevel inheritance works.

class Parent:
    def __init__(self, name, hair_color):
        self.name = name
        self.hair_color = hair_color
    def getName(self):
        return self.name
    def getHairColor(self):
        return self.hair_color

class Child(Parent):
    def __init__(self, name, hair_color, eye_color):
        super().__init__(name, hair_color)
        self.eye_color = eye_color
    def getEyeColor(self):
        return self.eye_color

class Grandchild(Child):
    def __init__(self, name, hair_color, eye_color, height, age):
        super().__init__(name, hair_color, eye_color)
        self.height = height
        self.age = age
    def getHeight(self):
        return self.height
    def getAge(self):
        return self.age

def description():
    return "{}, {} hair, {} eyes, Height: {} inches, {} years old.".format(tami.getName(), tami.getHairColor(), tami.getEyeColor(), tami.getHeight(), tami.getAge())

tami = Grandchild("Tamara", "Brown", "Brown", 63, 49)

print(description())
