class Calculadora:
    def __init__(self, operador, operando1, operando2):
        self.operador = operador
        self.operando1 = operando1
        self.operando2 = operando2

    def operacion(self):
       switch={
           '+':'suma',
           '-':'resta',
           '*':'producto',
           '/':'division',
           '^':'elevado'
       }


       method = getattr(self, switch.get(str(self.operador)))
       return method()

    def suma(self):
        return self.operando1 + self.operando2

    def resta(self):
        return self.operando1 - self.operando2

    def division(self):
        return self.operando1 / self.operando2

    def producto(self):
        return self.operando1 * self.operando2

    def elevado(self):
        res = self.operando1
        for x in range(0, int(self.operando2 - 1)):
            res *= self.operando1
        return res

print('Operando 1')
op1 = float(input())
print('Operando 2')
op2 = float(input())
print('Operador')
operador = str(input())
c = Calculadora(operador, op1, op2)
print( "Resultado : %s" %(str(c.operacion())))