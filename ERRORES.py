import logging
logging.basicConfig(filename = 'aplicacion.log',
                    level=logging.INFO,
                    format='%(asctime)s-%(levelname)s-%(message)s')

def validar (edad):
        if edad <0:
            logging.error('registraron una edad invalidad cod777')
            raise ValueError("no estabas ni en la imaginacion")
        elif edad >=0:
            print("la edad es valida")
            logging.info("EDAD VALIDA")
try:     
    validar(-10)
except ValueError as error:
    logging.warning("REGISTRARON UNA EDAD INVALIDA PERO CAPTURE EL ERROR")
    print(error)

