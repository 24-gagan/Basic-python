class Animal:
    def make_sound(self):
        print("Animal sound")
class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Dog barks")
d=Dog()
d.make_sound()