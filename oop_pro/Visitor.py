
class Guest:

    def press_bell(self, obj):
        return obj.ring()

class Employee(Guest):

    def press_finger(self, finger):
        return finger.input_fingerprints()

    def press_password(self,pwd):
        return pwd.input_password()



