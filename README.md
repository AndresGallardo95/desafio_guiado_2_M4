# desafio_guiado_2_M4

# Gran Fantasía

Bienvenido a **Gran Fantasía**, un sencillo juego de consola donde los jugadores pueden crear su propio personaje, enfrentarse a un orco y tomar decisiones para atacar o huir. Este proyecto ha sido desarrollado en Python, utilizando programación orientada a objetos.

## Descripción

Este proyecto consiste en dos archivos principales:

1. **personaje.py**: Contiene la clase `Personaje`, que es la base para crear y gestionar los personajes en el juego.
2. **juego.py**: Es el script principal que ejecuta el juego, permitiendo al jugador interactuar con su personaje y enfrentarse a un orco.

## Estructura del Proyecto

### personaje.py

Este archivo contiene la clase `Personaje`, que tiene los siguientes métodos:

- `__init__(self, nombre)`: Constructor que inicializa el nombre, nivel y experiencia del personaje.
- `obtener_estado(self)`: Retorna una cadena con el estado actual del personaje (nombre, nivel y experiencia).
- `asignar_experiencia(self, exp)`: Asigna experiencia al personaje, ajustando su nivel y experiencia acumulada en función de los puntos de experiencia recibidos o perdidos.
- `__lt__(self, otro_personaje)`: Compara si el nivel del personaje actual es menor que el de otro personaje.
- `__gt__(self, otro_personaje)`: Compara si el nivel del personaje actual es mayor que el de otro personaje.
- `calcular_probabilidad_ganar(self, otro_personaje)`: Calcula la probabilidad de que el personaje actual gane en un enfrentamiento contra otro personaje.
- `enfrentar_orco(probabilidad)`: Método estático que simula un enfrentamiento con un orco, determinando si el personaje gana o pierde en función de una probabilidad dada.

### juego.py

Este archivo contiene la función principal `main()` que ejecuta el juego. El flujo del juego es el siguiente:

1. Se da la bienvenida al jugador y se solicita el nombre de su personaje.
2. Se crea un personaje con el nombre proporcionado y se muestra su estado inicial.
3. Se crea un personaje enemigo (Orco) con el que el jugador se enfrentará.
4. Se calcula la probabilidad de ganar del jugador contra el orco.
5. El jugador elige si desea atacar o huir:
   - Si elige atacar, se determina aleatoriamente si gana o pierde el enfrentamiento.
   - Según el resultado, se actualizan los estados del jugador y del orco (experiencia y nivel).
   - Se muestra el estado actualizado de ambos personajes.
6. Si el jugador decide huir, el juego termina.

## Requisitos

Para ejecutar este juego, necesitas tener instalado:

- Python 3.x

## Ejecución del Juego

1. Clona el repositorio o descarga los archivos `personaje.py` y `juego.py`.
2. Abre una terminal y navega hasta el directorio donde se encuentran los archivos.
3. Ejecuta el siguiente comando para iniciar el juego:

   ```bash
   git clone https://github.com/AndresGallardo95/desafio_guiado_2_M4.git
