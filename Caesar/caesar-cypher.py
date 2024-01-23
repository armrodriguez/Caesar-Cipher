## Author: MrSh4d0w

## Desplazamiento para cifrado/descifrado
desplazamientoCifrado = 3

## Cifra mayusculas, minusculas, y los simbolos quedan igual
def cifradoCesarAlfabetoInglesMAY(cadena):
    """
    Devuelve un cifrado Cesar tradicional (+3)
    """
    # Definir la nueva cadena resultado
    resultado = ''

    desplazamientoCifrado = 3

    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])

        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):  # ¿Es esto una letra mayuscula?
            # print("LETRA CIFRADA minuscula " + str((ordenClaro-65) % 26))
            ordenCifrado = ((ordenClaro - 65 + desplazamientoCifrado) % 26) + 65  # Cifrado Caesar
            resultado = resultado + chr(ordenCifrado)
        elif (ordenClaro >= 97 and ordenClaro <= 122):
            # print("LETRA CIFRADA mayuscula " + str((ordenClaro - 97) % 26))
            ordenCifrado = ((ordenClaro - 97 + desplazamientoCifrado) % 26) + 97  # Cifrado Caesar
            resultado = resultado + chr(ordenCifrado)
        else: ##Añadir espacios o simbolos
            print("ES UN SIMBOLO " + chr(ordenClaro))
            resultado = resultado + chr(ordenClaro)


        # Añade el caracter cifrado al resultado
        i = i + 1
    # devuelve el resultado
    return resultado

## Descifrado
def descifradoCesarAlfabetoInglesMAY(cadena):
    """
    Devuelve un cifrado Cesar tradicional (+3)
    """
    # Definir la nueva cadena resultado
    resultado = ''

    desplazamientoCifrado = 3
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])

        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):  # ¿Es esto una letra mayuscula?
            ordenCifrado = ((ordenClaro - 65 - desplazamientoCifrado) % 26) + 65  # Cifrado Caesar
            resultado = resultado + chr(ordenCifrado)
        elif (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = ((ordenClaro - 97 - desplazamientoCifrado) % 26) + 97  # Cifrado Caesar
            resultado = resultado + chr(ordenCifrado)
        else: ##Añadir espacios o simbolos
            print("ES UN SIMBOLO " + chr(ordenClaro))
            resultado = resultado + chr(ordenClaro)

        # Añade el caracter cifrado al resultado
        i = i + 1
    # devuelve el resultado
    return resultado

claroCESARMAY = 'VENI VIDI VINCI AURIAzeaccvaw!'
print(claroCESARMAY)
cifradoCESARMAY = cifradoCesarAlfabetoInglesMAY(claroCESARMAY)
print(cifradoCESARMAY)
print(descifradoCesarAlfabetoInglesMAY(cifradoCESARMAY))
