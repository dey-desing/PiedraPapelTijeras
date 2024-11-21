print("¡Bienvenido a Piedra, Papel o Tijeras!")
opciones = ["piedra", "papel", "tijeras"]
jugador = input("Elige piedra, papel o tijeras: ")
print(f"Tú elegiste: {jugador}")

import random
sistema= random.choice(opciones)
print(f"El sistema eligió: {sistema}")

if jugador == sistema:
    print("Es un empate.")
elif (jugador == "piedra" and sistema == "tijeras") or \
     (jugador == "tijeras" and sistema == "papel") or \
     (jugador == "papel" and sistema == "piedra"):
    print("¡Ganaste!")
else:
    print("Perdiste.")