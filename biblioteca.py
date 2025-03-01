import logging, random, os, time


print("""
--  ######    ######  ######    ####     ######   #####   ######## #######   #####      ##
--   ##  ##     ##     ##  ##    ##        ##    ##   ##  #  ##  #  ##  ##  ##   ##    ####
--   ##  ##     ##     ##  ##    ##        ##    ##   ##     ##     ##      ##        ##  ##
--   #####      ##     #####     ##        ##    ##   ##     ##     ####    ##        ######
--   ##  ##     ##     ##  ##    ##        ##    ##   ##     ##     ##      ##        ##  ##
--   ##  ##     ##     ##  ##    ## ##     ##    ##   ##     ##     ##  ##  ##   ##   ##  ##
--  ######    ######  ######    ######   ######   #####     ####   #######   #####    ##  ##
""")
print()
print()
print()
print()


# USUARIOS VARIOS 
class User : 
    def __init__ (self):
        self.nombre = []
        self.apellido = []
        self.edad = []
        self.correo = []
        self.multas = []


#TITULOS EN PRESTAMO Y QUIEN LOS TIENE 
titulos_prestamo = {}
autores_prestamo = {}
genero_prestamo = {}

#BILBIOTECA 
class Libro:
    def __init__(self):
        self.titulos = []
        self.autor = []
        self.genero = []
        self.users_obj = User() 

# se crea un tiempo ramdom para luego compararlo con el plazo maximo de devolucion de libro
    def tiempo_de_prestamos (self):
        plazo = self.tiempo_prestamo + 5
        print(self.tiempo_prestamo)  
        self.tiempo_max = random.randint(1, plazo)



# DEVOLVER LOS LIBROS PRESTADOS 
    def devolver_titulos (self):
        print("-----------------------------------------------------")
        print(titulos_prestamo)
        if len(titulos_prestamo) == 0:
            print("**NO HAY TITULOS EN PRESTAMO**")
            self.menu_libro()
        else:
            user_devol = input("**CUAL ES EL USUARIO QUE VA A DEVOLVER EL LIBR0? \n").upper()
            if user_devol in self.users_obj.nombre:
                print("-----------------------------------------------------")
                print("TITULOS QUE TIENES: ", titulos_prestamo[user_devol])
                print("-----------------------------------------------------")
                print("AUTORES DE LOS LIBROS: ",autores_prestamo[user_devol])
                print("-----------------------------------------------------")
                print("GENERO DE LOS LIBROS: ", genero_prestamo[user_devol])
                print("-----------------------------------------------------")
                libro_devol = input("CUAL ES EL TITULO QUE VAS A DEVOLVER?? \n").upper()
                autor_devol = input("CUAL ES EL AUTOR DE ESE LIBRO? \n").upper()
                genero_devol = input("CUAL ES EL GENERO DE ESE LIBRO? \n").upper()

                if libro_devol in titulos_prestamo[user_devol] and autor_devol in autores_prestamo[user_devol] and genero_devol in genero_prestamo[user_devol]:
                    self.titulos.append(libro_devol)
                    self.autor.append(autor_devol)
                    self.genero.append(genero_devol)
                    titulos_prestamo.pop(user_devol)
                    autores_prestamo.pop(user_devol)
                    genero_prestamo.pop(user_devol)
                    self.tiempo_de_prestamos()

                    if self.tiempo_max > self.tiempo_prestamo:
                        print(f"TU PLAZO ERA DE {self.tiempo_prestamo} DIAS Y LO DEVOLVISTE EN {self.tiempo_max} DIAS")
                        multa = "5.000 $"
                        print(f"""!!ADEVERTENCIA¡¡
                                TIENES UNA MULTA DE {multa} POR 
                                NO ENTREGAR EL LIBRO EN EL PLAZO
                                                                """)
                        self.users_obj.multas.append(multa)
                        print(f"TUS MULTAS SON: {self.users_obj.multas}")
                        print(f"LISTA DE LIBROS EN LA BIBLIOTECA{self.titulos}")
                        print(f"LISTA DE AUTORES EN LA BIBLIOTECA{self.autor}")
                        print(f"LISTA DE GENEROS EN LA BIBLIOTECA{self.genero}")
                        self.menu_libro()
                    else:
                        print("NO TIENES MULTAS")
                    print(f"LISTA DE LIBROS EN LA BIBLIOTECA{self.titulos}")
                    print(f"LISTA DE AUTORES EN LA BIBLIOTECA{self.autor}")
                    print(f"LISTA DE GENEROS EN LA BIBLIOTECA{self.genero}")
                    self.menu_libro()
                else:
                    print("NO TIENES ESE LIBRO CON ESAS CARACTERISTICAS PARA DEVOLVER")
                    self.menu_libro()
            else:
                print("ESTE USUARIO NO SE ENCUNETRA EN LA BASE DE DATOS, AÑADELO EN EL MENU PRINCIPAL")
                self.menu_libro()


# AGREGAR UN USUARIO 
    def users (self):
        print("-----------------------------------------------------")
        nombres = input("INGRESA EL NOMBRE DEL USUARIO: \n").upper()
        self.users_obj.nombre.append(nombres)
        apellidos = input("INGRESA TU APELLIDO: \n").upper()
        self.users_obj.apellido.append(apellidos)
        edads = int(input("INGRESA TU EDAD: \n"))
        self.users_obj.edad.append(edads)
        correo = input("INGRESA TU CORREO ELECTRONICO: \n").upper()
        self.users_obj.correo.append(correo)
        print(f"BIENVENIDO {nombres}, {apellidos} GRACIAS POR CONTAR CON NOSOTROS, TU CORREO ES {correo}")
        self.menu_libro()

    #LISTA DE TITULOS PRESTADOS :
    def titulos_prestamos (self):
        print("-----------------------------------------------------")
        if len(titulos_prestamo) == 0:
            print("NO HAY TITULOS EN PRESTAMO") 
            self.menu_libro()
        else:
            print("ESTA ES LA LISTA DE TITULOS PRESTADOS")
            print(titulos_prestamo)
            print("ESTA ES LA LISTA DE AUTORES EN PRESTAMO")
            print(autores_prestamo)
            print("ESTA ES LA LISTA DE GENEROS EN PRESTAMO")
            print(genero_prestamo)
            self.menu_libro()

    # AGREGAR LIBROS A LA BIBLIOTECA 
    def agregar_libro (self):
        print("-----------------------------------------------------")
        agregar_libro = input("QUE LIBRO DESEAS AGREGAR A LA BIBLIOTECA?? \n").upper()
        self.titulos.append(agregar_libro)
        print(f"SE AGREGO ({agregar_libro})  A LA LIBRERIA ")
        agregar_autor = input(("CUAL ES EL AUTOR DEL LIBRO?: \n")).upper()
        self.autor.append(agregar_autor)
        print(f"SE AGREGO ({agregar_autor}) A LA LISTA DE AUTORES")
        agregar_genero = input("CUAL ES EL GENERO DEL LIBRO? \n").upper()
        self.genero.append(agregar_genero)
        print(f"SE AGREGO EL GENERO ({agregar_genero}) A LA LISTA DE GENEROS")
        self.menu_libro()
    
    #BUSCAR LIBROS 
    def buscar_libro(self):
        while True :
            print("-----------------------------------------------------")
            print("LISTA DE TITULOS: ",self.titulos)
            print("LISTA DE AUTORES ",self.autor)
            print("LISTA DE GENEROS ",self.genero)
            if (len(self.titulos)) == 0 :
                print("NO HAY NINGUN TITULO EN LA BILBIOTECA PARA BUSCAR, AÑADE UNO O ESPERA A QUE OTRO USUARIO DEVUELVA UNO")
                self.menu_libro()
            else:
                buscar_titulo = str(input("INGRESA EL TITULO A BUSCAR \n").upper())
                if buscar_titulo in self.titulos:
                    print(f"({buscar_titulo}) SE ENCUENTRA EN LA LISTA DE LIBROS DE LA BIBLIOTECA ")
                    otra_busqueda = (input("DESEAS BUSCAR OTRO LIBRO?? S/N \n").upper())
                    if otra_busqueda == "N":
                        self.menu_libro()
                else:
                    print(f"EL LIBRO ({buscar_titulo}) NO SE ENCUENTRA EN LA LISTA DE TITULOS DE LA BIBLIOTECA ")
                    otra_busqueda = (input("DESEAS BUSCAR OTRO LIBRO?? S/N \n").upper())
                    if otra_busqueda == "N":
                        self.menu_libro()

    #PRESTAR LIBROS 
    def prestar_libro(self):
        print("-----------------------------------------------------")
        print("CATALOGO DE LIBROS: ")
        print()
        print("TITULOS", self.titulos)
        print("AUTORES", self.autor)
        print("GENEROS", self.genero)
        if len(self.titulos) == 0 and len(self.autor) == 0  and len(self.genero) == 0 :
            print("LA LISTA DE TITULOS, AUTORES Y GENEROS ESTA VACIA, AÑADE UN LIBRO Y PODRAS CONTINUAR")
            self.menu_libro()
        print("-----------------------------------------------------")
        print()
        usuarios_prestar = input("A QUE USUARIO LE VAS A PRESTAR EL LIBRO? \n").upper()
        print()
        print("-----------------------------------------------------")
        
        if usuarios_prestar in self.users_obj.nombre:
            libro_prestar = input("QUE LIBRO QUIERES PRESTAR?? \n").upper()
            print("-----------------------------------------------------")
            autor_libro = input("CUAL ES EL AUTOR DEL LIBRO?? \n").upper()
            print("-----------------------------------------------------")
            genero_libro = input("CUAL ES EL GENERO DEL LIBRO?? \n").upper()
            print("-----------------------------------------------------")
            self.tiempo_prestamo = int(input("CUANTOS DIAS VAS A PRESTAR EL LIBRO?? \n"))
            if  libro_prestar in self.titulos and autor_libro in self.autor and genero_libro in self.genero:
                titulos_prestamo[usuarios_prestar] = libro_prestar
                autores_prestamo[usuarios_prestar] = autor_libro
                genero_prestamo[usuarios_prestar] = genero_libro
                self.titulos.remove(libro_prestar)
                self.autor.remove(autor_libro)
                self.genero.remove(genero_libro)
                print(f"SE PRESTO EL LIBRO {libro_prestar} AL USUARIO {usuarios_prestar}")
                print(f"LISTA DE TITULOS EN PRESTAMO SE ACTUALIZO: {titulos_prestamo}")
                self.menu_libro()
            else:
                print(f"EL LIBRO ({libro_prestar}) DEL AUTOR ({autor_libro}) DEL GENERO ({genero_libro}) NO SE ENCUENTRA EN LA LIBRERIA")
                self.menu_libro()
        else: 
            print(f"""EL USUARIO ({usuarios_prestar}) NO SE ENCUNETRA EN LA LISTA DE USUARIOS
                    POR FAVOR AÑADE EL USUARIO COMPLETANDO EL FORMULARIO.""")
            self.menu_libro()

# MENU INICIAL
    def menu_libro (self):
        terminal_cl()
        opcion = 0
        while opcion == 0:
            print("****************************************")
            opcion = int(input("""  MENU :
                            1. Agregar un Libro:
                            2. Agregar un nuevo usuario
                            3. Buscar libro 
                            4. Prestar libro
                            5. Lista de Libros Prestados 
                            6. Devolver Libro
                            7. Salir \n"""))
            if opcion == 1:
                self.agregar_libro()
            elif opcion == 2:
                self.users()
            elif opcion == 3:
                self.buscar_libro()
            elif opcion == 4:
                self.prestar_libro()
            elif opcion == 5:
                self.titulos_prestamos()
            elif opcion == 6:
                self.devolver_titulos()
            elif opcion == 7:
                print("SALIENDO...")
                time.sleep(2)
                terminal_cl()
                global salir
                salir = False

def terminal_cl():
    input("PRECIONA ENTER PARA CONTINUAR")
    os.system("cls")

#EJECUCION DEL PROGRAMA
def ejecutar ():
    biblioteca = Libro()
    biblioteca.menu_libro()

logging.basicConfig(filename= "BLIBLIOTECA.LOGS",
                    level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s')

salir = True
while salir == True:
    try :
        ejecutar()
    except ValueError as error:
        logging.error("EN EL MENU, NO SE ACEPTAN LETRAS")
        logging.warning(" EL ERROR FUE ENCAPSULADO")
        print("OPCION INVALIDA, POR FAVOR INGRESE UNA OPCION DEL 1 AL 7")