from personaje import Personaje

def main():
    print("¡Bienvenido a Gran Fantasía!")
    nombre_jugador = input("Por favor indique nombre de su personaje: ")
    
    jugador = Personaje(nombre_jugador)
    print(jugador.obtener_estado())
    
    orco = Personaje("Orco")
    
    while True:
        probabilidad = jugador.calcular_probabilidad_ganar(orco)
        print(f"¡Oh no!, ¡Ha aparecido un Orco!\nCon tu nivel actual, tienes {probabilidad*100}% de probabilidades de ganarle al Orco.")
        print("Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.")
        print("Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.")
        
        opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")
        
        if opcion == '1':
            resultado = Personaje.enfrentar_orco(probabilidad)
            if resultado == "Gana":
                print("¡Le has ganado al orco, felicidades!")
                jugador.asignar_experiencia(50)
                orco.asignar_experiencia(-30)
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                jugador.asignar_experiencia(-30)
                orco.asignar_experiencia(50)
            
            print(jugador.obtener_estado())
            print(orco.obtener_estado())
        elif opcion == '2':
            print("¡Has huido! El orco ha quedado atrás.")
            break

if __name__ == "__main__":
    main()
