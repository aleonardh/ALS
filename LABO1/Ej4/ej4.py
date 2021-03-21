import cmath
class Ej4:
    global pi
    pi = 3.14
    def area(radio):

        return pi*radio*radio

    def perimetre(radio):
        return pi * 2 * radio

    print("Dame radio circunferencia:")
    radio = input()
    radio = float(radio)
    print("Este es el area %f" %(area(radio)) )
    print("Este es el perimetre %f" %(perimetre(radio)) )
