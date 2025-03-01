#CLASE ARMAS Y SUS DERIVADAS COMO ANILLO MAGICO, PISTOLA DE ALTO CALIBRE ETC

class Arma:
    def __init__(self, color, daño):
        self.__color = color 
        self.__daño = daño 

class Anillo_Magico(Arma):
    def __init__(self, color, daño, tipo_magia):
        super().__init__(color, daño)
        self.__tipo_magia = tipo_magia
    
    def Descripcion (self):
        print(f"Este arma es de tipo magia: {self.__tipo_magia}, con daño {self.__daño} y de color {self.__color} ")

class Baston_Magico(Arma):
    def __init__(self, color, daño, tipo_magia):
        super().__init__(color, daño)
        self.__tipo_magia = tipo_magia
    
    def Descripcion(self):
        print(f"Este arma es de tipo magia: {self.__tipo_magia}, con daño {self.__daño} y de color {self.__color} ")

class Espada(Arma):
    def __init__(self, color, daño, tipo_metal):
        super().__init__(color, daño)
        self.__tipo_metal = tipo_metal
        
    def Descripcion(self):
        print(f"Este arma es de tipo espada con daño {self.__daño}, creado con {self.__tipo_metal} y de color {self.__color} ")

class Katana(Arma):
    def __init__(self, color, daño, tipo_metal):
        super().__init__(color, daño)
        self.__tipo_metal = tipo_metal
    
    def Descripcion(self):
        print(f"Este arma es de tipo espada con daño {self.__daño}, creado con {self.__tipo_metal} y de color {self.__color} ")

# CLASE PERSONAJE Y SUS DEVIRADAS COMO GUERRERO, MAGO 

class Personaje : 
    def __init__(self,vida, poder, clase):
        self.vida = vida 
        self.poder = poder 
        self.clase = clase

class Mago(Personaje):
    def __init__(self, vida, poder, clase, arma_magica):
        super().__init__(vida, poder, clase)
        self.arma_magica = arma_magica
    
    def Descripcion (self):
        print(f"Este personaje es de tipo {self.clase}, su vida es {self.vida}, su poder es {self.poder}.")

class Guerrero(Personaje):
    def __init__(self, vida, poder, clase, tipo_espada):
        super().__init__(vida, poder, clase)
        self.__tipo_espada = tipo_espada

    def Descripcion (self):
        print(f"Este personaje es de tipo {self.clase}, su vida es {self.vida}, su poder es {self.poder}.")

# FASE DE INSTANCIAR OBJETOS 
Anillo_Fuego = Anillo_Magico("Rojo",25, "Fuego")
Anillo_Agua = Anillo_Magico("Azul", 25, "Agua")
Anillo_Tierra = Anillo_Magico("Cafe", 25, "Tierra")
Anillo_Aire = Anillo_Magico("Gris", 25, "Aire")
#------------------------------------------------
Baston_De_Dragon = Baston_Magico("Rojo", 25, "Aliento de Dragon")
Baston_De_Las_Aguas = Baston_Magico("Azul", 25, "Dominio del Agua")
#------------------------------------------------
Espada_hierro = Espada("Plata", 50, "Hierro")
Espada_Obsidiana = Espada("Negro", 70, "Obsidiana")

Merlin = Mago(100, 50, "Mago", Anillo_Agua)
Merlin.Descripcion()

Midas = Guerrero(150,50,"Guerrero", Espada_hierro)
Midas.Descripcion()