# Crear un programa que solicite una cadena de texto al usuario y determine si
# la primera palabra tiene al menos una letra mayúscula en la segunda
# posición.

while(1):
    
    cadena = str(input("Ingrese un texto : "))
    cadena = cadena.split()[0]
    
    if(cadena[1] == cadena[1].upper()):
        print("En la primera palabra SI hay una mayuscula en la segunda posicion.")
    else:
        print("En la primera palabra NO hay una mayuscula en la segunda posicion.")
    print()

