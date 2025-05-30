import os

#==============================================OPCION 3==============================================#

def menu_consultas(inversiones, clientes, acciones, acciones_valores): #QUE SE REPITA#
    opcion = ""
    while opcion != "9":
        os.system('cls')
        print("             === Consultas ===")
        print("1. Cantidad total de acciones adquiridas por usuario")
        print("2. Promedio de acciones adquiridas de cada empresa entre todos los usuarios")
        print("3. Usuarios ordenados alfabéticamente de la Z-A junto con el total invertido en las distintas empresas")
        print("4. Inversión total acumulada por toda la cartera de usuarios")
        print("5. Por cada usuario, la empresa en la que compró más acciones")
        print("6. Acción con mayor inversión total (USD) en toda la cartera")
        print("7. Porcentaje de inversión por usuario respecto a la inversión total acumulada")
        print("8. Listado de los usuarios cuya inversión total supere la inversión promedio")
        print("9. Salir del menú de consultas")
        opcion = input("Ingrese una opción (1-9): ")
        
        match opcion:
            case "1":
                os.system('cls')
                print("=== Cantidad total de acciones adquiridas por usuario ===\n")
                print("     Usuarios        Acciones")
                for i in range(len(clientes)):
                    cantidad,valor = sumar_acciones(inversiones, acciones_valores, i, 0)
                    print(f"{clientes[i]:<17} |     {cantidad}")
                    print("-----------------------------")
                os.system('pause')
                
            case "2":
                os.system('cls')
                print("=== Promedio de acciones de cada empresa ===")
                print("Empresa   Acciones")
                for i in range(len(acciones)):
                    cantidad,valor = sumar_acciones(inversiones, acciones_valores, i, 1)
                    print(f"{acciones[i]:<8}|  {cantidad/len(clientes):.2f}")
                    print("----------------")
                os.system('pause')
                
            case "3":
                os.system('cls')
                print("=== Usuarios por usuario ordenados alfabéticamente ===\n")
                clientes_ord_pocision = [] #para saber el usuario a la que la matriz hace referencia cuando se ordene
                clientes_orden_alfabetico = [] #matriz que vamos a ordenar alfabéticamente
                clientes_orden_alfabetico += clientes#matriz que vamos a ordenar alfabéticamente
                ordenar(clientes_orden_alfabetico)
                
                # guardamos la posición de cada cliente en la matriz original
                for i in range(len(clientes_orden_alfabetico)):
                    for j in range(len(clientes_orden_alfabetico)):
                        if clientes_orden_alfabetico[i] == clientes[j]:
                            clientes_ord_pocision += [j]
                
                # mostramos los clientes ordenados alfabéticamente junto con el total invertido en cada empresa
                for i in range(len(clientes_orden_alfabetico)):
                    print(f"{clientes_orden_alfabetico[i]}:")
                    for j in range(len(acciones)):
                        print(f"    {acciones[j]}: {sumar_acciones_2(inversiones, 0, clientes_ord_pocision[i], 1, j)} acciones")
                    print("------------------------")
                os.system('pause')
                
            case "4":
                os.system('cls')
                total,inversores = valor_total_invertido(inversiones, acciones_valores)
                print("=== Inversión total acumulada por toda la cartera de usuarios ===\n")
                print("                         $",total,"\n")
                os.system('pause')
                
            case "5":
                os.system('cls')
                print("=== Empresa en la que cada usuario compró más acciones ===\n")
                for i in range(len(clientes)):
                    max_acciones = -1
                    empresa_max = ""
                    for j in range(len(acciones)):
                        cantidad = sumar_acciones_2(inversiones, 0, i, 1, j)
                        if cantidad > max_acciones:
                            max_acciones = cantidad
                            empresa_max = acciones[j]
                    print(f"{clientes[i]:<18} | {empresa_max:<7}| {max_acciones}")
                print("------------------------")
                os.system('pause')
                
            case "6":
                os.system('cls')
                print("=== Accion con mayor inversion ===")
                max_acciones = -1
                empresa_max = ""
                for i in range(len(acciones)):
                    cantidad,valor = sumar_acciones(inversiones, acciones_valores, i, 1)
                    if cantidad > max_acciones:
                        max_acciones = cantidad
                        empresa_max = acciones[i]
                print("           ---------------")
                print(f"           | {empresa_max:<7}| {max_acciones} |")
                print("           ---------------")
                os.system('pause')
                
            case "7":
                os.system('cls')
                print("=== Porcentaje de inversión por usuario ===\n")
                print("     Usuarios        Porcentaje")
                total,inversores = valor_total_invertido(inversiones, acciones_valores)
                for i in range(len(clientes)):
                    cantidad,valor = sumar_acciones(inversiones, acciones_valores, i, 0)
                    porcentaje = (valor/ total) * 100
                    print(f"{clientes[i]:<18} |  {porcentaje:.2f}%")
                os.system('pause')
            case "8":
                os.system('cls')
                print("=== Usuarios con inversión mayor al promedio ===\n")
                total,inversores = valor_total_invertido(inversiones, acciones_valores)
                promedio = total / inversores
                print(f"Promedio de inversión: {promedio:.2f}")
                print("-----------------------------")
                print("     Usuarios        Inversión")
                for i in range(len(clientes)):
                    cantidad,valor = sumar_acciones(inversiones, acciones_valores, i, 0)
                    if total == 0:
                        print("No hay inversiones registradas.")
                        os.system('pause')
                        return
                    elif valor > promedio:
                        print(f"{clientes[i]:<18} |  {valor:.2f}")
                os.system('pause')
            case "9":
                return
            case _:
                print("Opción inválida")
                os.system('pause')


#opcion 1 & 2#
def sumar_acciones(inversiones, acciones_valores, comparacion, parametro):
    suma = 0
    suma_valor = 0
    for i in range(len(inversiones)):
        if inversiones[i][parametro] == comparacion:
            suma += inversiones[i][2]
            suma_valor += inversiones[i][2] * acciones_valores[inversiones[i][1]]
    return suma, suma_valor

#opcion 3#
#funcion para ordenar alfabéticamente una lista
def ordenar(muestra):
    for i in range(len(muestra)):
        for j in range(len(muestra)-1):
            if muestra[j]>muestra[i]:
                aux_inversion=muestra[j]
                muestra[j]=muestra[i]
                muestra[i]=aux_inversion
    return muestra

#funcion para sumar acciones de un usuario en una empresa específica
def sumar_acciones_2(inversiones, parametro_1, comparacion_1, parametro_2, comparacion_2):
    suma = 0
    for i in range(len(inversiones)):
        if inversiones[i][parametro_1] == comparacion_1 and inversiones[i][parametro_2] == comparacion_2:
            suma += inversiones[i][2]
    return suma

#opcion 4#

def valor_total_invertido(inversiones, acciones_valores):
    total = 0
    cantidad_inversores = 0
    for i in range(len(inversiones)):
        match inversiones[i][1]:
            case 0:
                total += inversiones[i][2] * acciones_valores[0]
            case 1:
                total += inversiones[i][2] * acciones_valores[1]
            case 2:
                total += inversiones[i][2] * acciones_valores[2]
        if total != 0:
            cantidad_inversores += 1
    return total, cantidad_inversores

#opcion 5#

#opcion 6#

#opcion 7#

#opcion 8#