import os

class GestorDeContraseñas:
    def __init__(self):
        self.contrasena = "UTH123"

    def verificarContraseña(self, contrasenaIngresada):
        if contrasenaIngresada == self.contrasena:
            print("Contraseña correcta. Acceso permitido.")
        else:
            print("Contraseña incorrecta. Acceso denegado.")
            exit()