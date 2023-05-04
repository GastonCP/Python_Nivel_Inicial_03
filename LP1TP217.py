# .Crear un programa que solicite una cadena de texto al usuario y determine si
# la primera palabra tiene la letra "i" en la última posición.

while(1):
    
    cadena = str(input("Ingrese un texto : "))
    cadena = cadena.lower()
    cadena = cadena.split()[0]

    if(cadena[len(cadena)-1] == "i"):
        print("El texto ingresado SI tiene I en el ultimo caracter de la primera palabra.")
    else:
        print("El texto ingresado NO tiene I en el ultimo caracter de la primera palabra.")
    print()