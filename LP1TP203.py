# Crear un programa que solicite una cadena de texto al usuario y determine si
# la primera palabra tiene al menos cuatro letras

while(1):
    cadena = str(input("Ingrese un texto : "))
    if(len(cadena) > 0 ):
        len(cadena.split()[0])

        if(len(cadena.split()[0]) >= 4):
            print("La primera palabra SI tiene al menos cuatro letras. (", len(cadena.split()[0]),")")
        else:
            print("La primera palabra NO tiene al menos cuatro letras. (", len(cadena.split()[0]),")")
        print()