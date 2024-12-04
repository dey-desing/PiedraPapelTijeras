import random
print("¡Bienvenido a Piedra, Papel o Tijeras!")

opciones = ["piedra", "papel", "tijeras"]
jugar_de_nuevo = True

puntaje_jugador = 0
puntaje_sistema = 0

while jugar_de_nuevo:
    
    jugador = input("Elige piedra, papel o tijeras: ")
    print(f"Tú elegiste: {jugador}")
    
    sistema= random.choice(opciones)
    print(f"El sistema eligió: {sistema}")
    
    if jugador == sistema:
        print("Es un empate.")
    elif (jugador == "piedra" and sistema == "tijeras") or \
     (jugador == "tijeras" and sistema == "papel") or \
     (jugador == "papel" and sistema == "piedra"):
        print("¡Ganaste!")
        puntaje_jugador += 1
    else:
        print("Perdiste.")
        puntaje_sistema += 1
        
    print (f"Puntaje: {puntaje_jugador} Jugador - {puntaje_sistema} Sistema")
    
    respuesta = input("Quieres jugar otra vez? (si/no):")
    if respuesta != "si":
        jugar_de_nuevo = False
        
print ("Gracias por jugar!")