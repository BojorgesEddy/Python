import random

numero = random.randrange(1,50)
jugador = int(input("Adivina el numero entre 1 a 50: \n"))
contador = 1

while jugador != numero:
    if jugador < numero:
        print("El numero es mas alto, intenta de nuevo.. ")
        seguir = input("quieres seguir jugando (s/n)").lower()
        if seguir == "n":
            print("gracias por jugar")
            jugador = numero
        else:
            jugador = int(input("\nAdivina el numero entre 1 a 50: \n"))
            contador = contador + 1     
    else:
        print("El numero es mas bajo, intenta de nuevo.. ")
        seguir = input("quieres seguir jugando (s/n)").lower()
        if seguir == "n":
            print("gracias por jugar")
            jugador = numero
        else:
            jugador = int(input("\nAdivina el numero entre 1 a 50: \n"))
            contador = contador + 1
              
print(f"El numero es {numero}")
print(f"Intentos {contador}")
        