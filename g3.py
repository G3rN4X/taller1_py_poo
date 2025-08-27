class saludo:
    #metodo constructor
    #se usa para inicializar obj
    def __init__(self, dato_texto):
        #atributo
        self.mensaje = dato_texto

    def get_mensaje(self):
        return self.mensaje

    def set_atributo(self, dato_nuevo_mensaje):
        self.mensaje = dato_nuevo_mensaje

    def tomar_nombre(self):
        nombre_usuario = input("escriba el nombre del usuario:")
        return nombre_usuario
    
    def crear_mensaje(self, dato_usuario):
        self.mensaje = "buenas usuario" + dato_usuario
        self.imprimir_mensaje(self.mensaje)  
    
    def imprimir_mensaje(self, dato_mensaje):
        print(dato_mensaje)

#codigo principal
texto= "bueenas usuario querido"

obj_mensaje = saludo(texto)

aux_dato = obj_mensaje.tomar_nombre()

obj_mensaje.crear_mensaje(aux_dato)


