import random
from getpass import getpass

# Diccionario para mapear los números a jugadas
jugadas = {
    1: "Piedra",
    2: "Papel",
    3: "Tijera",
    4: "Lagarto",
    5: "Spock"
}

# Función para determinar el ganador
def determinar_ganador(jugada1, jugada2):
    if jugada1 == jugada2:
        return "Empate"
    elif (jugada1 == 1 and jugada2 in [3, 4]) or \
         (jugada1 == 2 and jugada2 in [1, 5]) or \
         (jugada1 == 3 and jugada2 in [2, 4]) or \
         (jugada1 == 4 and jugada2 in [2, 5]) or \
         (jugada1 == 5 and jugada2 in [1, 3]):
        return "Usuario 1"
    else:
        return "Usuario 2"

# Función para jugar una ronda del juego
def jugar_ronda(versus):
    # Obtener jugada del usuario 1
    if versus:
        jugada_usuario1 = int(getpass('Usuario 1 - Ingresa tu elección (1: Piedra, 2: Papel, 3: Tijera, 4: Lagarto, 5: Spock): '))
        jugada_usuario2 = int(getpass('Usuario 2 - Ingresa tu elección (1: Piedra, 2: Papel, 3: Tijera, 4: Lagarto, 5: Spock): '))
    else:
        jugada_usuario1 = int(input('Ingresa tu elección (1: Piedra, 2: Papel, 3: Tijera, 4: Lagarto, 5: Spock): '))
        jugada_usuario2 = random.randint(1, 5)
        print(f'La jugada del ordenador es {jugadas[jugada_usuario2]}')

    print(f'La jugada del Usuario 1 es {jugadas[jugada_usuario1]}')
    print(f'La jugada del Usuario 2 es {jugadas[jugada_usuario2]}')

    ganador = determinar_ganador(jugada_usuario1, jugada_usuario2)
    if ganador == "Empate":
        print("Empate")
    else:
        print(f"Gana {ganador}")

    return ganador

# Función principal para el juego
def jugar():
    marcador = {"Usuario 1": 0, "Usuario 2": 0, "Empates": 0}
    modo_juego = input('Selecciona el modo de juego (1: vs Ordenador, 2: vs Usuario): ')
    versus = modo_juego == '2'
    
    while True:
        ganador = jugar_ronda(versus)
        if ganador != "Empate":
            marcador[ganador] += 1
        else:
            marcador["Empates"] += 1
        
        print(f'Marcador: Usuario 1: {marcador["Usuario 1"]}, Usuario 2: {marcador["Usuario 2"]}, Empates: {marcador["Empates"]}')
        
        continuar = input('¿Quieres jugar otra vez? (s/n): ')
        if continuar.lower() != 's':
            break

    print('Gracias por jugar!')

# Ejecutar el juego
jugar()
