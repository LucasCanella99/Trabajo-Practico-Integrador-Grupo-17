from mensaje import Mensaje
# from usuario import Usuario
# from carpeta import Carpeta

class ServidorCorreo:
    def __init__(self):
        self.__usuarios = {} #Acá vamos a guardar los usuarios, con su nombre y mail.
        self.__mensajes = [] #Acá vamos a guardar la lista de mensajes.

    def registrar_usuario(self,nombre,email):
        if email in self.__usuarios:
            raise ValueError('La dirección de email ya existe')
        
        usuario_nuevo = Usuario(nombre,email)
        self.__usuarios[email] = usuario_nuevo# elegimos un diccionario porque podemos buscar por la clave directamente y es mas rapido que recorrer una lista entera
        return 'El usuario: ' + str(nombre) + 'email: ' + str(email) +' Se ha registrado exitosamente.'
    

    def enviar_mensaje(self,mensaje):
        pass

    def recibir_mensaje(self):
        pass

    def listar_mensajes(self):
        pass