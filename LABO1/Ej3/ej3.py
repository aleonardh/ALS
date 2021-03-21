class Ej3:

    def dame_nombre():
        print("Hola!, dame tu nombre")
        nombre = input()
        return nombre

    def imprimir_nombre(nombre):
        print("Bienvenido, "+nombre)


    imprimir_nombre(dame_nombre())