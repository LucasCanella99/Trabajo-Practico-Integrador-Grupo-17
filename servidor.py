from abc import ABC, abstractmethod
from mensaje import Mensaje
from usuario import Usuario
from redservidores import RedServidores

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
    def __init__(self,dominio,red_servidores):
        self.__usuarios = {} #Acá vamos a guardar los usuarios, con su correo
        self.__dominio = dominio #Dominio del servidor, cada nodo del grafo va a tener un dominio en especifico
        self.__red_servidores = red_servidores 
        self.__red_servidores.agregar_servidor(dominio) #hacemos que por defecto al crear una instancia de servidor esta se agregue a la red de servidores

    def registrar_usuario(self,nombre,apellido, contraseña,correo):
        if correo in self.__usuarios:
            raise ValueError('La dirección de correo ya existe')
        
        correo_partes = correo.split('@') #Separamos el correo en dos partes. Nombre y dominio
        if len(correo_partes) != 2: # Verificamos que el correo este correctamente tipeado
            raise ValueError('El formato de correo es invalido')
        
        dominio_correo = correo_partes[1] #Obtenemos el dominio

        if dominio_correo != self.__dominio:
            raise ValueError('El servidor al que se esta intentando registrar solo registra usuario del dominio: ' + str(self.__dominio) + ' intente nuevamente.')

        usuario_nuevo = Usuario(nombre,apellido, contraseña,correo)
        self.__usuarios[correo] = usuario_nuevo# elegimos un diccionario porque podemos buscar por la clave directamente y es mas rapido que recorrer una lista entera
        return 'El usuario: ' + str(nombre) + str(apellido) + 'correo: ' + str(correo) +' Se ha registrado exitosamente.'
    
    def get_dominio(self):
        return self.__dominio

    def get_usuarios(self):
        return self.__usuarios.copy() #Por seguridad para que no haya modificaciones accidentales en el diccionario original

    def enviar_mensaje(self,mensaje,destinatario,remitente,asunto):
        prioridad_de_asignacion = 1

        if 'urgente' in asunto.lower(): # Si el asunto dice por ej "Facturas urgente" le cambia la prioridad a 0
            prioridad_de_asignacion = 0

        if remitente not in self.__usuarios:
            raise ValueError('El remitente no esta registrado en el sistema')
        remitente = self.__usuarios[remitente]
        mensaje_a_enviar = Mensaje(mensaje,destinatario,remitente,asunto,prioridad = prioridad_de_asignacion)#Se escribe el mensaje con todo lo que requiere
        dominio_remitente = self.__dominio
        dominio_destinatario = destinatario.split('@')[-1]
        #enrutamiento
        if dominio_remitente.lower() == dominio_destinatario.lower(): #caso que el dominio sea el mismo en ambos correos(mismo servidor) NIVEL LOCAL
            if destinatario not in self.__usuarios:
                raise ValueError('El destinatario no esta registrado en el sistema')
            destinatario = self.__usuarios[destinatario]
            destinatario.filtrar_mensaje(mensaje_a_enviar)
        else:
            ruta_red = self.__red_servidores.encontrar_ruta(dominio_remitente,dominio_destinatario)
            if isinstance(ruta_red, list):
                print('Ruta para enviar mensaje: ' + '->'.join(ruta_red))  # Simulacion del envio de mensajes NIVEL EXTERNO DISTINTOS SERVIDORES
            else:
                raise ValueError('Error al enviar el mensaje')
        remitente.guardar_mensaje_enviado(mensaje_a_enviar)


  

    def listar_mensajes(self,correo,tipo_de_bandeja): #En este metodo agregamos como parametro tipo_de_bandeja para que devuelva la de entrada o salida
        if correo not in self.__usuarios:
            raise ValueError('El usuario: ' + correo + ' no se encuentra registrado')
        
        usuario = self.__usuarios[correo]

        if tipo_de_bandeja == 'entrada':
            bandeja = usuario.get_bandeja_entrada()
            mensajes = bandeja.mensajes
            if mensajes: 
                print ('Bandeja de entrada del usuario: '+ correo + '\n') 
                for mensaje in mensajes:
                    print ('-'+ str(mensaje))
            else:
                print('La bandeja de entrada esta vacía.')
        
        elif tipo_de_bandeja == 'salida':
            bandeja = usuario.get_bandeja_salida()
            mensajes = bandeja.mensajes
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
        cantidad_mensajes = len(bandeja.mensajes)

        return 'El usuario ' + str(correo) + ' tiene: ' + str(cantidad_mensajes) + ' mensajes.'



        

        
        



