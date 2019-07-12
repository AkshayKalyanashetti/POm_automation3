from dummy.demo import Xyz
class X:
    def __init__(self, name):
        Xyz.__init__(self, 23)
        self.b = name
        print(self.b)
a = X('akshay')

