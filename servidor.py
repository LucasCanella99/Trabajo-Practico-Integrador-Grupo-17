from abc import ABC, abstractmethod
from mensaje import Mensaje
from usuario import Usuario

class InterfazBasica(ABC):
    @abstractmethod
    def enviar_mensaje(self,mensaje,destinatario,remitente,asunto): 
        pass
    @abstractmethod
    def listar_mensajes(self,correo,bandeja):
        pass
    @abstractmethod
    def registrar_usuario(self,nombre,apellido, contraseña,correo):
        pass
    @abstractmethod
    def recibir_mensaje(self,correo):
        pass

    

class ServidorCorreo(InterfazBasica):
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

  

    def listar_mensajes(self,correo,tipo_de_bandeja): #En este metodo agregamos como parametro tipo_de_bandeja para que devuelva la de entrada o salida
        if correo not in self.__usuarios:
            raise ValueError('El usuario: ' + correo + ' no se encuentra registrado')
        
        usuario = self.__usuarios[correo]

        if tipo_de_bandeja == 'entrada':
            bandeja = usuario.get_bandeja_entrada()
            mensajes = bandeja.lista_de_mensajes()
            if mensajes: 
                print ('Bandeja de entrada del usuario: '+ correo + '\n') 
                for mensaje in mensajes:
                    print ('-'+ str(mensaje))
            else:
                print('La bandeja de entrada esta vacía.')
        
        elif tipo_de_bandeja == 'salida':
            bandeja = usuario.get_bandeja_salida()
            mensajes = bandeja.lista_de_mensajes()
            if mensajes: 
                print ('Bandeja de salida del usuario: '+ correo + '\n') 
                for mensaje in mensajes:
                    print ('-'+ str(mensaje) )
            else:
                print('La bandeja de salida esta vacía.')
        else:
            raise ValueError('El tipo de bandeja debe ser "entrada" ó "salida"')


    def recibir_mensaje(self,correo): # hicimos que este metodo de la cantidad de mensajes recibidos, porque enviar mensajes ya hace que el destinatario, reciba el mensaje y que listar mensaje, los muestre.
        if correo not in self.__usuarios:
            raise ValueError('El usuario: ' + correo + ' .No se encuentra registrado')
        
        usuario = self.__usuarios[correo]
        bandeja = usuario.get_bandeja_entrada()
        mensajes = bandeja.lista_de_mensajes()
        cantidad_mensajes = len(mensajes)

        return 'El usuario ' + str(correo) + ' tiene: ' + str(cantidad_mensajes) + ' mensajes.'



        

        
        



