# Crear un programa que solicite una cadena de texto al usuario y determine si
# la primera letra de la primera palabra es una vocal.

def EsVocal( caracter : chr):
    if caracter == "a" :
        return True
    elif caracter == "e" : 
        return True
    elif caracter == "i" : 
        return True
    elif caracter == "o" : 
        return True
    elif caracter == "u" : 
        return True
    else :
        return False 

while(1):
    cadena = str(input("Ingrese un texto : "))
    cadena = cadena.lower()
    indice = 0

    if(cadena[indice] == " "):
        while (cadena[indice] == " "):
            indice = indice + 1

    if(EsVocal(cadena[indice])):
        print("El caracter inicial de la primera palabra SI es vocal. (",cadena[indice],")")
    else:
        print("El caracter inicial de la primera palabra NO es vocal. (",cadena[indice],")")
    print()