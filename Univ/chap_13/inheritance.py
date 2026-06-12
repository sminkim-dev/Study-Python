class Parent:
    def __init__(self, name):
        self.name = name
    def to_str(self):
        return self.name
class Child(Parent):
    def __init__(self, name):
        super().__init__(name)
    def to_str(self):
        return self.name

p = Parent("parent")
c = Child("child")
print(p.to_str())
print(c.to_str())