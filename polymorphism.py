class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    print("Dog sound")
class Cat(Animal):
    def sound(self):
        print("Cat sound")
def make_sound(animal):
    animal.sound()
a=Animal()
b=Dog()
c=Cat()
make_sound(a)
make_sound(b)
make_sound(c)