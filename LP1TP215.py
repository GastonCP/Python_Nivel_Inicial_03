# Crear un programa que solicite una cadena de texto al usuario y
# determine si la primera palabra tiene al menos una letra minúscula.

while(1):
    
    cadena = str(input("Ingrese un texto : "))
    if(len(cadena) > 0 ):
        cadena = cadena.split()[0]

        contadorDeMinusculas = 0
        for i in range (len(cadena)):  
            if( cadena[i]== cadena[i].lower()):
                contadorDeMinusculas = contadorDeMinusculas + 1

        if(contadorDeMinusculas > 0):
            print("El texto ingresado SI tiene minusculas (",contadorDeMinusculas,").")
        else:
            print("El texto ingresado NO tiene minusculas.")
        print()