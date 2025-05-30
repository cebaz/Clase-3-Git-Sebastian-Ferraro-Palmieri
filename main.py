import os
from validaciones import *
from opcion_1 import *
from opcion_2 import *
from opcion_3 import *

# Inicialización de vectores y matriz
clientes = [
    "Lunatico_pixel", "Sombra_cristal", "Ecoerrante", "Navefantasma", "Bytesdelabahia",
    "Tintaenelviento", "Relojoxidado", "Miradacodificada", "Circuitoazul", "Fuego_niebla",
    "Teclaerrante", "Nebulosa_urbana", "Sueño_binario", "Saltofantasma", "Claveoculta"
]

acciones = ["APPLE", "TESLA", "NVIDIA"]
acciones_valores = [10.41, 7.71, 8.50]
inversiones = []

#===============================================MAIN===============================================#

opcion = ""
while opcion != "4":
    os.system('cls')
    print("=== Sistema de Gestión de Inversiones - UTN-Capital ===")
    print("1. Registrar una transacción")
    print("2. Visualizar todos los datos")
    print("3. Consultas")
    print("4. Salir")
    opcion = input("Ingrese una opción (1-4): ")         ###validacion###
    
    match opcion:
        case "1":
            registrar_transaccion(inversiones, clientes, acciones, acciones_valores)
        case "2":
            visualizar_datos(inversiones, clientes, acciones, acciones_valores)
        case "3":
            menu_consultas(inversiones, clientes, acciones, acciones_valores)
        case "4":
            os.system('cls')
            print("Programa finalizado.")
        case _:
            print("\nOpción inválida")
            os.system('pause')
