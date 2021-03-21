import statistics
class Uno:
    def __init__(self, sec):
        self.sec = sec

    def media(self):
        res = 0
        for x in self.sec:
            res += x

        return res / len(self.sec)

    def mayor(self):
        return max(self.sec)

    def menor(self):
        return min(self.sec)

    def desviacion(self):
        return statistics.stdev(self.sec)

sec = []
print("Ingresa numeros:")
x = float(input())
while x != 0:
    sec.append(x)
    x = float(input())

c = Uno(sec)
print("Media: %f" %(c.media()))
print("Mayor: %f" %(c.mayor()))
print("Menor: %f" %(c.menor()))
print("Desviacion Típica: %f" %(c.desviacion()))



