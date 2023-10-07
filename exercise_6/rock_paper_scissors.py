from random import randint
choice = ["piedra","papel","tijeras"]

computer = choice[randint(0,2)]


print("Bienvenido al juego de piedra, papel y tijeras\n")
jugador = input("Escoge una: ").lower()
print("Eleccion de la computadora: "+computer)

if jugador == computer:
    print("empate")
elif jugador == "piedra" and computer == "papel":
    print("perdiste")
elif jugador == "piedra" and computer == "tijeras":
     print("ganaste")
elif jugador == "papel" and computer == "tijeras":
     print("perdiste")
elif jugador == "papel" and computer == "piedra":
     print("ganaste")
elif jugador == "tijeras" and computer == "piedra":
     print("perdiste")
elif jugador == "tijeras" and computer == "papel":
     print("ganaste")