class Coordenates:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def fmt_coordenadas(self):
        return "(%s , %s) " %(str(self.n1), str(self.n2))


print("Give me first number")
x = input()
print("Give me second number")
y = input()
c = Coordenates (x, y)
print("Your coordenates are: %s" %(c.fmt_coordenadas()))
