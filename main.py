jugfutbol_dict = {
    "Lamine Yamal":"Jugador  del FC Barcelona extremo derecho",
    "Lionel Andres Messi":"Jugador  del Inter Miami Delantero centro y 2do maximo goleador de la historia",
    "Cristiano Ronaldo":"Jugador  del Al Nassr Delantero centro y maximo goleador de la historia",
    "Neymar Jr":"Jugador del Santos FC Delantero centro",
    "Ronaldinho Gaucho":"Jugador actualmente retirado pero historico del FC Barcelona Medio centro o Delantero"
}

jugador = input("Digita el jugador que quieres aprender")

if jugador in jugfutbol_dict.keys():
    print(jugfutbol_dict[jugador])
else:
    print("Debes escribir correctamente el jugador o inicial en mayuscula o prueba otro")
