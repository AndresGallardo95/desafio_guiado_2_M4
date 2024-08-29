class Personaje:
    """
    Clase que representa un personaje en el juego "Gran Fantasía".

    Atributos:
        nombre (str): El nombre del personaje.
        nivel (int): El nivel actual del personaje, inicializado en 1.
        experiencia (int): La cantidad de experiencia acumulada por el personaje, inicializada en 0.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Personaje.

        Args:
            nombre (str): El nombre del personaje.
        """
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        """
        Obtiene el estado actual del personaje.

        Returns:
            str: Una cadena que contiene el nombre, nivel y experiencia del personaje.
        """
        return f'NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}'

    def asignar_experiencia(self, exp):
        """
        Asigna experiencia al personaje, ajustando su nivel y experiencia acumulada.

        Args:
            exp (int): La cantidad de experiencia a asignar. Puede ser positiva o negativa.
        
        Nota:
            - Si la experiencia acumulada alcanza o supera los 100 puntos, el nivel del personaje
              aumenta y se ajusta la experiencia restante.
            - Si la experiencia cae por debajo de 0 y el personaje tiene un nivel superior a 1, 
              el nivel disminuye y se ajusta la experiencia restante.
        """
        nueva_experiencia = self.experiencia + exp
        
        while nueva_experiencia >= 100:
            nueva_experiencia -= 100
            self.nivel += 1
            
        while nueva_experiencia < 0 and self.nivel > 1:
            nueva_experiencia += 100
            self.nivel -= 1
        
        self.experiencia = max(0, nueva_experiencia)

    def __lt__(self, otro_personaje):
        """
        Compara si este personaje es de menor nivel que otro.

        Args:
            otro_personaje (Personaje): El otro personaje con el que se compara.
        
        Returns:
            bool: True si este personaje tiene un nivel menor que el otro, False en caso contrario.
        """
        return self.nivel < otro_personaje.nivel

    def __gt__(self, otro_personaje):
        """
        Compara si este personaje es de mayor nivel que otro.

        Args:
            otro_personaje (Personaje): El otro personaje con el que se compara.
        
        Returns:
            bool: True si este personaje tiene un nivel mayor que el otro, False en caso contrario.
        """
        return self.nivel > otro_personaje.nivel

    def calcular_probabilidad_ganar(self, otro_personaje):
        """
        Calcula la probabilidad de ganar en un enfrentamiento contra otro personaje.

        Args:
            otro_personaje (Personaje): El otro personaje con el que se enfrenta.
        
        Returns:
            float: La probabilidad de ganar como un valor entre 0.33 y 0.66.
            - 0.66 si el personaje es de mayor nivel.
            - 0.33 si el personaje es de menor nivel.
            - 0.5 si ambos personajes están en el mismo nivel.
        """
        if self > otro_personaje:
            return 0.66
        elif self < otro_personaje:
            return 0.33
        else:
            return 0.5

    @staticmethod
    def enfrentar_orco(probabilidad):
        """
        Simula un enfrentamiento con un orco basado en la probabilidad de ganar.

        Args:
            probabilidad (float): La probabilidad de ganar, un valor entre 0 y 1.
        
        Returns:
            str: "Gana" si el personaje gana el enfrentamiento, "Pierde" en caso contrario.
        """
        from random import uniform
        resultado = "Gana" if uniform(0, 1) <= probabilidad else "Pierde"
        return resultado
