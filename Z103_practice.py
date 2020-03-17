
class cycle():
    def __init__(self):
        self.name = "ram"
        self.age = "10"

    def update(self):
        self.age = 12
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = cycle()
c2 = cycle()

if c1.compare(c2):
   print("They are same age.")
else:
   print("b")





