from mensaje import Mensaje
from usuario import Usuario


class ServidorCorreo:
    def __init__(self):
        self.__usuarios = {} #Acá vamos a guardar los usuarios, con su correo

    def registrar_usuario(self,nombre,apellido, contraseña,correo):
        if correo in self.__usuarios:
            raise ValueError('La dirección de correo ya existe')
        
        usuario_nuevo = Usuario(nombre,apellido, contraseña,correo)
        self.__usuarios[correo] = usuario_nuevo# elegimos un diccionario porque podemos buscar por la clave directamente y es mas rapido que recorrer una lista entera
        return 'El usuario: ' + str(nombre) + str(apellido) + 'correo: ' + str(correo) +' Se ha registrado exitosamente.'
    
    def get_usuarios(self):
        return self.__usuarios.copy() #Por seguridad para que no haya modificaciones accidentales en el diccionario original

    def enviar_mensaje(self,mensaje,destinatario,remitente,asunto):
        if destinatario not in self.__usuarios:
            raise ValueError('El destinatario no esta registrado en el sistema')
        if remitente not in self.__usuarios:
            raise ValueError('El remitente no esta registrado en el sistema')
        destinatario = self.__usuarios[destinatario]#Obtenemos los objeto Usuario de destinatario y abajo de remitente
        remitente = self.__usuarios[remitente]
        mensaje_a_enviar = Mensaje(mensaje,destinatario.correo,remitente.correo,asunto)#Se escribe el mensaje con todo lo que requiere
        remitente.guardar_mensaje_enviado(mensaje_a_enviar)#Guardamos en la bandeja de salida
        destinatario.guardar_mensaje_recibido(mensaje_a_enviar)#Lo guardamos en la bandeja de entrada del destinatario

    def listar_mensajes_entrada(self,correo):
        if correo not in self.__usuarios:
            raise ValueError('El usuario no se encuentra registrado')
        
        usuario = self.__usuarios[correo]

        bandeja = usuario.get_bandeja_entrada()#Usamos los metodos de la clase Usuario para obtener los mensajes 
        mensajes = bandeja.lista_de_mensajes()

        if mensajes: 
            print (f'Bandeja de entrada del usuario {correo}: \n') # Si mensajes es True(tenia mensajes), que tiene contenido se ejecuta esta linea
            for mensaje in mensajes:
                print (f'-{mensaje}')
        else:
            print(f'La bandeja de entrada esta vacía.')# Si mensajes es False(No tenia mensajes) se ejecuta esta linea     
    
    def listar_mensajes_salida(self,correo):
        if correo not in self.__usuarios:
            raise ValueError('El usuario no se encuentra registrado')
        
        usuario = self.__usuarios[correo]

        bandeja = usuario.get_bandeja_salida()
  
        
        mensajes = bandeja.lista_de_mensajes()

        if mensajes: 
            print (f'Bandeja de salida del usuario {correo}: \n') # Si mensajes es True(tenia mensajes), que tiene contenido se ejecuta esta linea
            for mensaje in mensajes:
                print (f'-{mensaje}')
        else:
            print(f'La bandeja de salida esta vacía.')# Si mensajes es False(No tenia mensajes) se ejecuta esta linea  

        
        



