def es_numero_romano(cadena:str) -> bool:
    """
    recive una cadena
    verifica si contiene solo números romanos
    retorna True si es así, False en caso contrario
    """
    if cadena != "":
        retorno = False
    retorno = True
    for i in range(len(cadena)):
        if cadena[i] != "I" and cadena[i] != "V" and cadena[i] != "X" and cadena[i] != "L" and cadena[i] != "C" and cadena[i] != "D" and cadena[i] != "M":
            retorno = False
            break
    return retorno

#solicitar la cadena a verificar
cadena=input("Ingrese una cadena de caracteres: ")

#verificar si la cadena contiene solo numeros romanos
if es_numero_romano(cadena):
    print("La cadena SOLO tine números romanos.")
else:
    print("La cadena NO solo tine números romanos.")