from personaje import Personaje

def main():
    """
    Función principal que ejecuta el juego "Gran Fantasía".

    El juego permite al usuario crear un personaje, enfrentarse a un orco y decidir
    si atacar o huir. Dependiendo del resultado de los ataques, los estados del personaje
    y del orco se actualizan en consecuencia.

    El flujo del juego es el siguiente:
    1. Se da la bienvenida al jugador y se solicita el nombre de su personaje.
    2. Se crea el personaje del jugador y se muestra su estado inicial.
    3. Se crea un personaje enemigo ("Orco") con el que el jugador se enfrentará.
    4. Se calcula la probabilidad de ganar del jugador contra el orco.
    5. El jugador elige si desea atacar o huir:
       - Si ataca, se determina aleatoriamente si gana o pierde el enfrentamiento.
       - Se actualizan las experiencias y niveles de ambos personajes en función del resultado.
       - Se muestra el estado actualizado de ambos personajes.
       - Si el jugador decide huir, el juego termina.
    """

    print("¡Bienvenido a Gran Fantasía!")
    nombre_jugador = input("Por favor indique nombre de su personaje: ")
    
    # Crear el personaje del jugador
    jugador = Personaje(nombre_jugador)
    print(jugador.obtener_estado())
    
    # Crear el personaje enemigo (Orco)
    orco = Personaje("Orco")
    
    # Bucle principal del juego
    while True:
        # Calcular la probabilidad de ganar del jugador contra el orco
        probabilidad = jugador.calcular_probabilidad_ganar(orco)
        print(f"¡Oh no!, ¡Ha aparecido un Orco!\nCon tu nivel actual, tienes {probabilidad*100}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        
        # Solicitar al jugador que elija entre atacar o huir
        opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")
        
        if opcion == '1':
            # Determinar el resultado del ataque
            resultado = Personaje.enfrentar_orco(probabilidad)
            if resultado == "Gana":
                print("¡Le has ganado al orco, felicidades!")
                jugador.asignar_experiencia(50)
                orco.asignar_experiencia(-30)
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                jugador.asignar_experiencia(-30)
                orco.asignar_experiencia(50)
            
            # Mostrar los estados actualizados de ambos personajes
            print(jugador.obtener_estado())
            print(orco.obtener_estado())
        elif opcion == '2':
            # El jugador decide huir, termina el juego
            print("¡Has huido! El orco ha quedado atrás.")
            break

if __name__ == "__main__":
    main()
