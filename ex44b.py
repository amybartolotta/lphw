class Parent(object):

    def override(self):
        print("PARENT ovveride()")

class Child(Parent):

dad = Parent()
son = Child()

dad.override()
son.override()