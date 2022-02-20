import random 


def jugar():
    usuario = input("escoge una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijeta.\n ").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    if usuario == computadora:
        return '¡Empate!'
    
    if gano_el_jugador(usuario,computadora):
        return 'Ganaste groso'

    return 'Perdiste'


def gano_el_jugador(jugador, openente):
    # retonar el true (verdadero) si gana el jugador.
    #Piedra gana a tijera (pi>ti)
    #Tijera gana a Papel (ti>pa)
    #Papel gana a Piedra (pa>pi)
    if ((jugador == 'pi' and openente == 'ti')
        or (jugador == 'ti' and openente == 'pa')
        or (jugador == 'pa' and openente == 'pi')):
        return True

    else:
        return False


print(jugar())
