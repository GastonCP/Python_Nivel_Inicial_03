# Crear un programa que solicite una cadena de texto al usuario y determine si
# la primera palabra comienzan con la letra "a".

while(1):
    cadena = str(input("Ingrese un texto : "))
    if(len(cadena) > 0 ):
        cadena = cadena.lower()
        cadena = cadena.split()[0]

        if(cadena[0] == "a"):
            print("El caracter inicial de la primera palabra SI es A.")
        else:
            print("El caracter inicial de la primera palabra NO es A -> (",cadena[0],").")
        print()