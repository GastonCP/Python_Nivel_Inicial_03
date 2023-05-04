# Crear un programa que solicite una cadena de texto al usuario y determine si
# todas las palabras contienen la letra "e".

while(1):
    
    cadena = str(input("Ingrese un texto : "))
    if(len(cadena) > 0 ):
        cadena = cadena.lower()
        cantidadDePalabras = len(cadena.split())

        contadorE = 0
        for i in range (cantidadDePalabras):
            if( "e" in cadena.split()[i]):
                contadorE = contadorE + 1

        if(contadorE == cantidadDePalabras):
            print("En las", cantidadDePalabras, "palabras SI estan presntes las E.")
        else:
            print("En las", cantidadDePalabras, "palabras NO estan presntes las E.")
        print()