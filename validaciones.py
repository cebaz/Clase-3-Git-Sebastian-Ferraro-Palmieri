def validar_es_int(cadena):
    retorno = True
    for i in range(len(cadena)):
        if not (ord(cadena[i]) >= 48 and ord(cadena[i]) <= 57):
            retorno = False
            break
    return retorno

def validar_mayusculas(cadena):
    resultado = ""
    for caracter in cadena:
        if ord(caracter) >= 65 and ord(caracter) <= 90:
            resultado += chr(ord(caracter) + 32)
        else:
            resultado += caracter
    return resultado