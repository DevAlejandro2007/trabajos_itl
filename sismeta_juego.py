#CLASE ARMAS Y SUS DERIVADAS COMO ANILLO MAGICO, ESPADAS ETC

class Arma:
    def __init__(self, color, daño):
        self.color = color 
        self.daño = daño 

class Anillo_Magico(Arma):
    def __init__(self, color, daño, tipo_magia):
        super().__init__(color, daño)
        self.__tipo_magia = tipo_magia
    
    def Descripcion (self):
        return (f"ES DE TIPO MAGIA : {self.__tipo_magia}, CON DAÑO  {self.daño} Y DE COLOR  {self.color} ")
    
class Baston_Magico(Arma):
    def __init__(self, color, daño, tipo_magia):
        super().__init__(color, daño)
        self.__tipo_magia = tipo_magia
    
    def Descripcion(self):
        return (f"ES TIPO MAGIA: {self.__tipo_magia}, CON DAÑO {self.daño} Y DE COLOR {self.color} ")

class Espada(Arma):
    def __init__(self, color, daño, tipo_metal):
        super().__init__(color, daño)
        self.__tipo_metal = tipo_metal
        
    def Descripcion(self):
        print(f"ES UNA ESPADA TIPO: {self.daño}, CREADA CON {self.__tipo_metal} Y DE COLOR  {self.color} ")


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
        print(f"TU PERSONAJE ES DE TIPO {self.clase}, SU VIDA ES {self.vida}, SU PODER ES  {self.poder}.")

    def mi_arma(self):
        print(f"EL ARMA DE ESTE PERSONAJE ES {self.arma_magica}")
    
    def echizo_fuerte(self):
        print(f"**LANZA UN HECHIZO FUERTE CON SU {self.arma_magica}")
    
    def echizo_devil(self):
        print(f"LANZA UN HECHIZO FUERTE  CON TU {self.arma_magica }PERO ESPERAS A QUE SE RECARGUE TU ARMA 3 SEGUNDOS**")


class Guerrero(Personaje):
    def __init__(self, vida, poder, clase, tipo_espada):
        super().__init__(vida, poder, clase)
        self.tipo_espada = tipo_espada

    def Descripcion (self):
        print(f"ESTE PERSONAJE ES DE TIPO {self.clase}, SU VIDA ES {self.vida},SU PODER ES  {self.poder}")
    
    def mi_arma(self):
        return(f"EL ARMA DE ESTE PERSONAJE ES {self.tipo_espada}")
    
    def ataque_devil(self):
        print("**LANZA UN GOLPE DEVIL**")
    
    def ataque_fuerte(self):
        print("**LANZA UN ATAQUE FUERTE PERO QUEDA CANSADO DURANTE 2 SEGUNDOS**")

# CREACION DE PERSONAJE 
def Inicio ():
    print("** INICIANDO **")
    print("** CREANDO PERSONAJE **")
    eleccion = int(input(""" ESCOGE TU PERSONAJE 
                1. Mago
                2. Guerrero
                3 Salir
                """))
    if eleccion == 1:
        personaje = creacion_personaje_mago()
        personaje.Descripcion()
        personaje.mi_arma()
    elif eleccion == 2:
        personaje = creacion_personaje_guerrero()
        personaje.Descripcion()
        personaje.mi_arma()
    elif eleccion == 3:
        print("**SALIENDO**")
    else:
        raise ValueError("ELECCION INVALIDA")

#ESCOJE ARMA DEL GUERRERO


def elige_arma_guerrero():
    #------------------------------------------------
    Espada_hierro = Espada("Plata", 50, "Hierro")   
    Espada_Obsidiana = Espada("Negro", 70, "Obsidiana")
    #------------------------------------------------
    try:
        arma = int(input("""ESCOGE TU ESPADA 
1. Espada de Hierro (MUCHA DURAVILIDAD, DAÑO MEDIANO)
2. Espada de Obsidiana (POCA DURAVILIDAD, MUCHO DAÑO)
"""))
        if arma == 1:
            return Espada_hierro.Descripcion()
        else:
            return Espada_Obsidiana.Descripcion()
    except ValueError as Error:
        elige_arma_guerrero()


# ESCOJER TIPO DE ARMA MAGICA 
def elige_arma_magica():
    #---------------------------------------------
    Anillo_Fuego = Anillo_Magico("Rojo",25, "Fuego")
    Anillo_Agua = Anillo_Magico("Azul", 25, "Agua")
    Anillo_Tierra = Anillo_Magico("Cafe", 25, "Tierra")
    Anillo_Aire = Anillo_Magico("Gris", 25, "Aire")
    #---------------------------------------------
    Baston_De_Dragon = Baston_Magico("Rojo", 25, "Aliento de Dragon")
    Baston_De_Las_Aguas = Baston_Magico("Azul", 25, "Dominio del Agua")
    #---------------------------------------------
    try:
        arma = int(input("""ESCOGE TU ARMA MAGICA: 
1.Anillo Magico
2. Baston Magico  
"""))
    except ValueError():
        elige_arma_magica()
    try:
        if arma == 1:
            tipo_arma = int(input(""" ESCOJE EL TIPO DE ANILLO
    1. Anillo de Fuego
    2. Anillo de Tierra
    3. Anillo de Aire 
    4. Anillo de Agua
    """))
            if tipo_arma == 1:
                return Anillo_Fuego.Descripcion()
            elif tipo_arma == 2:
                return Anillo_Tierra.Descripcion()
            elif tipo_arma == 3: 
                return Anillo_Aire.Descripcion()
            elif tipo_arma == 4:
                return Anillo_Agua.Descripcion()
            else:
                    print("ESE ANILLO NO EXISTE, INTENTALO DE NUEVO")
                    elige_arma_magica()
        elif arma == 2:
            try:
                tipo_arma = int(input("""ELIGE TU TIPO DE BASTON MAGICO:
    1. BASTON DE DRAGON
    2. BASTON DE LAS AGUAS 
    """))
                if tipo_arma == 1:
                    return Baston_De_Dragon.Descripcion()
                else:
                    return Baston_De_Las_Aguas.Descripcion()
            except ValueError as error :
                elige_arma_magica()
    except ValueError as error :
        elige_arma_magica()
        
#CREAR PERSONAJE MAGICO  
def creacion_personaje_mago():
    personaje_mago = Mago( 100 , 20 , input("QUE TIPO DE MAGO SERA?  "),elige_arma_magica() )
    personaje_mago2 = Mago( 100 , 20 , input("QUE TIPO DE MAGO SERA?  "),elige_arma_magica() )
    return personaje_mago

# CREAR PERSONAJE GUERRERO  
def creacion_personaje_guerrero():
    personaje_guerrero = Guerrero(100 ,50, input("QUE TIPO DE GUERRERO SERA?  "),elige_arma_guerrero())
    return personaje_guerrero


try:
    Inicio()
except ValueError as error:
    print("OPCION NO VALIDA, VOLVIENDO AL INICIO ")
    Inicio()
    
