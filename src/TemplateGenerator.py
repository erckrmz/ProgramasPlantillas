import os

#print("File one __name__ is set to: {}" .format(__name__))

def startProgram() -> int:
    clear = lambda: os.system('cls')
    clear()
    print("Hola! Bienvenido al generador de plantillas para el Manual de Gestión de Proyectos.\n")
    print("Para empezar, primero debes seleccionar si deseas obtener la plantilla del manual en blanco"+
          " o deseas ingresar información "+
          "sobre la etapa 0 para llenar algunos datos automaticamente.\n")
    print("(1) Generar plantillas en blanco\n(2) Ingresar datos para precargar plantillas\n")
    
    while True:
        x=input("Respuesta: ")
        if((x!="1" and x!="2") or x is None):
            print("ERROR: La opción no es válida\nINTENTALO DE NUEVO\n")
        else:
            break

    return int(x)

if __name__ == "__main__":
    x=startProgram()
    print(x)