import random
#Bienvenida
print("¡Bienvenido a Piedra, Papel o Tijeras!")

#Opciones del juego
opciones = ["piedra", "papel", "tijeras"]

jugar_de_nuevo = True #Variable booleana actúa como controlador del bucle

#Contador de puntajes
puntaje_jugador = 0
puntaje_sistema = 0

while jugar_de_nuevo:
    #Entrada del jugador
    jugador = input("Elige piedra, papel o tijeras: ")
    print(f"Tú elegiste: {jugador}")
    #Elección del sistema
    sistema= random.choice(opciones)
    print(f"El sistema eligió: {sistema}")
    #Reglas del juego
    if jugador == sistema:
        print("Es un empate.")
    elif (jugador == "piedra" and sistema == "tijeras") or \
    (jugador == "tijeras" and sistema == "papel") or\
    (jugador == "papel" and sistema == "piedra"):
        print("¡Ganaste!")
        puntaje_jugador += 1
    else:
        print("Perdiste.")
        puntaje_sistema += 1
    #Puntajes
    print (f"Puntaje: {puntaje_jugador} Jugador - {puntaje_sistema} Sistema")
    #Jugar de nuevo
    respuesta = input("Quieres jugar otra vez? (si/no):")
    if respuesta != "si":
        jugar_de_nuevo = False #Variable booleana
#Terminar juego       
print ("Gracias por jugar!")