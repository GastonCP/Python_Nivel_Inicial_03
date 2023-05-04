# Crear un programa que solicite una cadena de texto al usuario y determine si
# la primera letra de la primera palabra es una vocal.

while(1):
    cadena = str(input("Ingrese un texto : "))
    if(len(cadena) > 0 ):
        cadena = cadena.lower()
        palabra = cadena.split()[0]
        if(palabra[0] in ["a","e","i","o","u"]):
            print("El caracter inicial de la primera palabra SI es vocal. (",palabra[0],")")
        else:
            print("El caracter inicial de la primera palabra NO es vocal. (",palabra[0],")")
        print()