print("Welcome to Malhotra Service Center")


class scooter_owner:
    def servecing(self, scooty):
        print("Please do the service of my scooty. ")
        scooty.vehicle()
class Outerlooker:
    def vehicle(self):
        print("repaired")

s5 = Outerlooker()
o1 = scooter_owner()
o1.servecing(s5)
