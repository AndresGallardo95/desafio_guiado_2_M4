class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def obtener_estado(self):
        return f'NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}'

    def asignar_experiencia(self, exp):
        nueva_experiencia = self.experiencia + exp
        
        while nueva_experiencia >= 100:
            nueva_experiencia -= 100
            self.nivel += 1
            
        while nueva_experiencia < 0 and self.nivel > 1:
            nueva_experiencia += 100
            self.nivel -= 1
        
        self.experiencia = max(0, nueva_experiencia)

    def __lt__(self, otro_personaje):
        return self.nivel < otro_personaje.nivel

    def __gt__(self, otro_personaje):
        return self.nivel > otro_personaje.nivel

    def calcular_probabilidad_ganar(self, otro_personaje):
        if self > otro_personaje:
            return 0.66
        elif self < otro_personaje:
            return 0.33
        else:
            return 0.5

    @staticmethod
    def enfrentar_orco(probabilidad):
        from random import uniform
        resultado = "Gana" if uniform(0, 1) <= probabilidad else "Pierde"
        return resultado

