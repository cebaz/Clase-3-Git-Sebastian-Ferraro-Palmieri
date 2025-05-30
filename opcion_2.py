import os

#==============================================OPCION 2==============================================#

def visualizar_datos(inversiones, clientes, acciones, acciones_valores):
    os.system('cls')
    
    inversiones_orden_alfabetico=ordenar_inversiones(inversiones, clientes)
    
    print("                     === Datos de Inversiones ===")
    print("      Usuario       |   Acción  |   Precio    |Cantidad|   Total invertido")
    for i in range(len(inversiones_orden_alfabetico)):
        usuario = clientes[inversiones_orden_alfabetico[i][0]]
        accion = acciones[inversiones_orden_alfabetico[i][1]]
        precio = acciones_valores[inversiones_orden_alfabetico[i][1]]
        cantidad = inversiones_orden_alfabetico[i][2]
        total = precio * cantidad
        print(f"{usuario:<20}|   {accion:<8}|   ${precio:<8.2f}|   {cantidad:<6}|   ${total:.2f}")
    os.system('pause')

def ordenar_inversiones(inversiones, clientes):
    #creamos una copoia de la matriz inversiones
    inversiones_orden_alfabetico = []
    for i in range(len(inversiones)):
        inversiones_orden_alfabetico += [inversiones[i]]
        
    #ordenamos la matriz inversiones_orden_alfabetico por orden alfabetico de los clientes
    for i in range(len(inversiones_orden_alfabetico)):
        for j in range(len(inversiones_orden_alfabetico)-1):
            if clientes[inversiones_orden_alfabetico[j][0]]>clientes[inversiones_orden_alfabetico[i][0]]:
                aux_inversion=inversiones_orden_alfabetico[j]
                inversiones_orden_alfabetico[j]=inversiones_orden_alfabetico[i]
                inversiones_orden_alfabetico[i]=aux_inversion
    return inversiones_orden_alfabetico