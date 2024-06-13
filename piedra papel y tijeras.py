import random

# Diccionario para convertir números a jugadas
jugadas = {1: "Piedra", 2: "Papel", 3: "Tijera"}

# Selección de la jugada del usuario
print('Selecciona el valor de jugada del usuario.')
print('\t1.- Piedra')
print('\t2.- Papel')
print('\t3.- Tijera')

# Manejo de entrada del usuario con validación
jugada_usuario = 0
while jugada_usuario not in [1, 2, 3]:
    try:
        jugada_usuario = int(input('Ingresa tu elección (1, 2, o 3): '))
        if jugada_usuario not in [1, 2, 3]:
            print('Valor incorrecto. Ingrésalo nuevamente.')
    except ValueError:
        print('Entrada no válida. Por favor ingresa un número (1, 2, o 3).')

# Selección de la jugada del ordenador
jugada_ordenador = random.randint(1, 3)

# Mostrar jugadas del usuario y del ordenador
print(f'La jugada del usuario es {jugadas[jugada_usuario]}')
print(f'La jugada del ordenador es {jugadas[jugada_ordenador]}')

# Determinación del ganador
# Empate
if jugada_usuario == jugada_ordenador:
    print('Empate')
# Gana el usuario
elif (jugada_usuario == 1 and jugada_ordenador == 3) or \
     (jugada_usuario == 2 and jugada_ordenador == 1) or \
     (jugada_usuario == 3 and jugada_ordenador == 2):
    print('Gana usuario')
# Gana el ordenador
else:
    print('Gana ordenador')

# Mostrar valor de jugada del ordenador
print(f'Valor de jugada del ordenador: {jugada_ordenador}')

# Repetición del juego
while True:
    repetir = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if repetir == 's':
        # Volvemos a pedir la jugada del usuario
        jugada_usuario = 0
        while jugada_usuario not in [1, 2, 3]:
            try:
                jugada_usuario = int(input('Ingresa tu elección (1, 2, o 3): '))
                if jugada_usuario not in [1, 2, 3]:
                    print('Valor incorrecto. Ingrésalo nuevamente.')
            except ValueError:
                print('Entrada no válida. Por favor ingresa un número (1, 2, o 3).')
        
        # Nueva jugada del ordenador
        jugada_ordenador = random.randint(1, 3)
        
        # Mostrar jugadas del usuario y del ordenador
        print(f'La jugada del usuario es {jugadas[jugada_usuario]}')
        print(f'La jugada del ordenador es {jugadas[jugada_ordenador]}')
        
        # Determinación del ganador
        if jugada_usuario == jugada_ordenador:
            print('Empate')
        elif (jugada_usuario == 1 and jugada_ordenador == 3) or \
             (jugada_usuario == 2 and jugada_ordenador == 1) or \
             (jugada_usuario == 3 and jugada_ordenador == 2):
            print('Gana usuario')
        else:
            print('Gana ordenador')
        
        print(f'Valor de jugada del ordenador: {jugada_ordenador}')
    elif repetir == 'n':
        print('Gracias por jugar.')
        break
    else:
        print('Opción no válida. Por favor ingresa "s" para sí o "n" para no.')
