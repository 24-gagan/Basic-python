class Parent:
    def parent_one(self):
        print("This is parent one")
class Parent2:
    def parent_two(self):
        print("This is parent two")
class Child(Parent,Parent2):
    def child(self):
        print("This is child class")
c=Child()
c.child()
c.parent_one()
c.parent_two()