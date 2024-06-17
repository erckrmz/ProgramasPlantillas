import os

def startProgram() -> int:
    os.system('cls')
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

def generateEmptyTemplate() -> int:
    os.system('cls')
    print("\nHas seleccionado la opción para generar las plantillas EN BLANCO.")
    print("\nPara continuar debes seleccionar alguno de los siguientes:\n")
    print("(1) Generar manual completo en blanco (genera un solo archivo con todas las etapas y plantillas, sin información)")
    print("(2) Generar manual por etapas en blanco (genera un archivo diferente para cada etapa, sin información)")
    print("(3) Volver al menú anterior")
    print("(4) Salir")
    while True:
        x=input("Respuesta: ")
        if((x!="1" and x!="2" and x!="3" and x!="4") or x is None):
            print("ERROR: La opción no es válida\nINTENTALO DE NUEVO\n")
        else:
            break
    return int(x)
    

def generateFulfilledTemplate() -> int:
    os.system('cls')
    print("\nHas seleccionado la opción para generar las plantillas CON INFORMACIÓN.")
    print("\nPara continuar debes seleccionar alguno de los siguientes:\n")
    print("(1) Generar manual completo con datos (genera un solo archivo con todas las etapas y plantillas, con información)")
    print("(2) Generar manual por etapas datos (genera un archivo diferente para cada etapa, con información)")
    print("(3) Volver al menú anterior")
    print("(4) Salir")
    while True:
        x=input("Respuesta: ")
        if((x!="1" and x!="2" and x!="3" and x!="4") or x is None):
            print("ERROR: La opción no es válida\nINTENTALO DE NUEVO\n")
        else:
            break
    return int(x)

