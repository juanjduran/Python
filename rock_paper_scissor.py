"""
Piedra, Papel, Tijeras

Es un popular juego para dos jugadores.
Cualquier jugador puede ejecutar una jugada con sus manos con estas opciones que tenemos disponible a continuación:

piedra (puño cerrado)
papel (mano plana)
tijeras (un puño con el dedo índice y el dedo medio extendidos, formando una V)
"""

import random

# Funcion que define el mensaje que se muestra cuando el jugador selecciona una opcion y la CPU crea un numero
# aleatorio que sera el indice de una lista que contiene las tres opciones del juego (piedra, papel, tijera)
# a - sera el nombre del jugador
# b - sera la opcion selecionada por el jugador
# c - sera la lista de opciones a elegir por el jugador
# d - sera la opcion aleatoria que creara la CPU

def message(a, b, c, d):
    return print(f"\n{a} eligio {c[b - 1]} y la CPU eligio {d}.")

game = ["PIEDRA", "PAPEL", "TIJERA"]
player = str(input("NOMBRE JUGADOR: "))
result = {1: "EMPATE!", 2: "PUNTO PARA CPU!", 3: f"PUNTO PARA {player}!"}
player_points = 0
cpu_points = 0
deuce_points = 0


while True:
    try:
        computer = random.choice(game)
        opc = int(input("\nSeleccione jugada:\n\n1-Piedra\n2-Papel\n3-Tijera\n\nOPCION: "))
        if opc == 1 and computer == "PIEDRA":
            message(player, opc, game, computer)
            print(result.get(1))
            deuce_points += 1
        elif opc == 1 and computer == "PAPEL":
            message(player, opc, game, computer)
            print(result.get(2))
            cpu_points += 1
        elif opc == 1 and computer == "TIJERA":
            message(player, opc, game, computer)
            print(result.get(3))
            player_points += 1
        elif opc == 2 and computer == "PIEDRA":
            message(player, opc, game, computer)
            print(result.get(3))
            player_points += 1
        elif opc == 2 and computer == "PAPEL":
            message(player, opc, game, computer)
            print(result.get(1))
            deuce_points += 1
        elif opc == 2 and computer == "TIJERA":
            message(player, opc, game, computer)
            print(result.get(2))
            cpu_points += 1
        elif opc == 3 and computer == "PIEDRA":
            message(player, opc, game, computer)
            print(result.get(1))
            deuce_points += 1
        elif opc == 3 and computer == "PAPEL":
            message(player, opc, game, computer)
            print(result.get(2))
            cpu_points += 1
        elif opc == 3 and computer == "TIJERA":
            message(player, opc, game, computer)
            print(result.get(3))
            player_points += 1
        else:
            print("\nLa opcion seleccionada no existe.")
        menu = input("\nJugar otra partida? S/N")
        if menu == "n" or menu == "N":
            break
    except ValueError:
        print("\nOpcion incorrecta. Debe elegir una opcion valida.")
print(f"\nRESULTADOS:\n\n{player}:{player_points}\nCPU:{cpu_points}\nEMPATES:{deuce_points}")



