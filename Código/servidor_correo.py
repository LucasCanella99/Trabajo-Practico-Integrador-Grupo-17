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

    def listar_mensajes(self,email):
        if email not in self.__usuarios:#verificamos que el email para listar los mensajes exista
            raise ValueError('El usuario no existe.')
        usuario = self.__usuarios[email] #accedemos al usuario en la lista(Ya registrado)
        bandeja_de_entrada = usuario.get_bandeja_entrada()#Accedemos a la bandeja de entrada de Usuario con su getter, que es un objeto de Carpeta (bandeja de entrada)
        if bandeja_de_entrada is None:
            raise ValueError('El usuario no tiene una bandeja de entrada')
        
        mensajes = bandeja_de_entrada.get_mensajes()#Usamos el getter de Usuario para poder tener los mensajes
        if not mensajes:
            print('El usuario no tiene mensajes')
        else:
            print(f'Mensajes del usuario: {email} \n')
            for mensaje in mensajes:
                print(mensaje)# usamos el str de la clase Mensaje

