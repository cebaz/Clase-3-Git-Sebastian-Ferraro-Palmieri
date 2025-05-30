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
inversiones = [
    [0, 0, 10],    # Lunatico_pixel invirtió en APPLE (10 unidades)
    [0, 1, 20],    # Lunatico_pixel invirtió en TESLA (20 unidades)
    [1, 1, 10],    # Sombra_cristal invirtió en TESLA (10 unidades)
    [1, 2, 20],    # Sombra_cristal invirtió en NVIDIA (20 unidades)
    [2, 2, 10],    # Ecoerrante invirtió en NVIDIA (10 unidades)
    [2, 0, 20],    # Ecoerrante invirtió en APPLE (20 unidades)
    [3, 0, 15],    # Navefantasma invirtió en APPLE (15 unidades)
    [4, 1, 25],    # Bytesdelabahia invirtió en TESLA (25 unidades)
    [5, 2, 30],    # Tintaenelviento invirtió en NVIDIA (30 unidades)
    [6, 1, 12],    # Relojoxidado invirtió en TESLA (12 unidades)
]

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
