# Crear un programa que solicite una cadena de texto al usuario y determine si
# todas las palabras tienen la letra "a" en la segunda posición.

while(1):
    
    cadena = str(input("Ingrese un texto : "))
    if(len(cadena) > 0 ):
        cadena = cadena.lower()
        cantidadDePalabras = len(cadena.split())

        contadorA = 0
        for i in range (cantidadDePalabras):
            
            palabra = cadena.split()[i]
            if( palabra[1]== "a"):
                contadorA = contadorA + 1

        if(contadorA == cantidadDePalabras):
            print("De las", cantidadDePalabras, "palabras, SI estan presentes las A en la segunda posicion.")
        else:
            print("En almenos 1 palabra, NO estan presentes las A en la segunda posicion.")
        print()
