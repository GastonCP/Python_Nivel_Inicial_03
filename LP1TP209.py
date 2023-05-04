# Crear un programa que solicite una cadena de texto al usuario y determine si
# la primera palabra tiene al menos una letra mayúscula.

while(1):
    
    cadena = str(input("Ingrese un texto : "))
    cadena = cadena.split()[0]

    contadorDeMayusculas = 0

    for i in range (len(cadena)):
        if(cadena[i] == cadena[i].upper()):
            contadorDeMayusculas = contadorDeMayusculas + 1
    
    if(contadorDeMayusculas > 0):
        print("La primera palabra SI hay mayusculas (", contadorDeMayusculas,").")
    else:
        print("La primera palabra NO contiene mayusculas.")
    print()