import os
from validaciones import *
#==============================================OPCION 1==============================================#

def registrar_transaccion(inversiones, clientes, acciones, acciones_valores):
    usuario_encontrado = -1
    while usuario_encontrado == -1:
        os.system('cls')
        usuario_input = input("Ingrese nombre del usuario: ")
        for i in range(len(clientes)):
            if clientes[i] == usuario_input:
                usuario_encontrado = i
                break
        
        if usuario_encontrado == -1:
            print("\nUsuario no encontrado.")
            os.system('pause')
            continue
    
    empresa_encontrada = -1
    while empresa_encontrada == -1:
        os.system('cls')
        empresa_input = input("Ingrese nombre de la empresa\nAPPLE: $10.41\nTESLA: $7.71\nNVIDIA: $8.50\n\n")
        for j in range(len(acciones)):
            if acciones[j] == empresa_input:
                empresa_encontrada = j
                break
    
        if empresa_encontrada == -1:
            print("\nEmpresa no encontrada.")
            os.system('pause')
            continue
    
    cantidad = -1
    while cantidad > 500 or cantidad < 0:
        os.system('cls')
        cantidad_input = input("Ingrese la cantidad de acciones: ")
        
        if validar_es_int(cantidad_input):
            cantidad = int(cantidad_input)
        else:
            print("\nCantidad inválida. Solo se permiten números.")
            os.system('pause')
            continue
        
        if cantidad > 500 or cantidad < 0:
            print("\nCantidad inválida. Debe ser entre 0 y 500.")
            os.system('pause')
            continue
        
    # Guardar la transacción en la matriz
    guardar_transaccion(inversiones, usuario_encontrado, empresa_encontrada, cantidad)
    print("Transacción registrada correwctamente")
    print("Total invertido: ", cantidad * acciones_valores[empresa_encontrada])
    os.system('pause')

def guardar_transaccion(inversiones, usuario, empresa, cantidad):
    # Guardar la transacción en la matriz
    fila = [usuario, empresa, cantidad]
    inversiones+=[fila]