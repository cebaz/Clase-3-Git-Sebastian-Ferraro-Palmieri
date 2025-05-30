def validar_es_int(cadena):
    retorno = True
    for i in range(len(cadena)):
            if cadena[i] not in "0123456789":
                retorno = False
                break
    return retorno