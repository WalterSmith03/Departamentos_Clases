class ImpresordNumerosImpares:
    def imprimirNumerosImpares(self):
        numero = int(input("Ingrese un número entero positivo: "))
        print("\nNumeros impares desde 1 hasta", numero, ":")
        for i in range(1, numero + 1):
            if i % 2 != 0:
                print(i)