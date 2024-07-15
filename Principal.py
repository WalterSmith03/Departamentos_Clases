import os

from GestorDeContraseñas import GestorDeContraseñas
from GestorDeUbicaciones import GestorDeUbicaciones
from CalculadoraDePromedios import CalculadoraDePromedios
from ImpresordNumerosImpares import ImpresordNumerosImpares

os.system('cls' if os.name == 'nt' else 'clear')

gestorDeContraseñas = GestorDeContraseñas()
gestorDeContraseñas.verificarContraseña(input("Ingresa la contraseña: "))

gestorDeUbicaciones = GestorDeUbicaciones()
calculadoraDePromedios = CalculadoraDePromedios()
impresorDeNumerosImpares = ImpresordNumerosImpares()

while True:
    print("\nMenu:")
    print("1. Inspeccionar los departamentos")
    print("2. Inspeccionar los municipios")
    print("3. Calcular promedio")
    print("4. Mostrar números impares")
    print("5. Salir")
    print("")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("")
        departamento = input("Ingrese el nombre del departamento: ")
        if departamento in gestorDeUbicaciones.departamentos:
            print("\nMunicipios del departamento:")
            print("")
            for municipio, codigo in gestorDeUbicaciones.departamentos[departamento].items():
                print(f"{municipio} - {codigo}")
        else:
            print("Departamento no encontrado.")
    elif opcion == "2":
        gestorDeUbicaciones.imprimirResultados()
    elif opcion == "3":
        calculadoraDePromedios.calcularPromedio()
    elif opcion == "4":
        impresorDeNumerosImpares.imprimirNumerosImpares()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion no válida. Por favor, seleccione una opción del menú.")