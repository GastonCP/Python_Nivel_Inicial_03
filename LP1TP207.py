# Crear un programa que solicite una cadena de texto al usuario y determine si
# la primera palabra tiene la letra "o" en la tercera posición

while(1):
    cadena = str(input("Ingrese un texto : "))
    if(len(cadena) > 0 ):
        cadena = cadena.lower()
        cadena = cadena.split()[0]

        if(cadena[2] == "o"):
            print("SI contiene O en la tercera posicion")
        else:
            print("NO contiene O en la tercera posicion")
        print()
