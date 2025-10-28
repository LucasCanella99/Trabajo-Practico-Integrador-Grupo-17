class Mensaje:
    def __init__(self,mensaje,destinatario,remitente,asunto,prioridad=0):
        self.__mensaje = mensaje
        self.__destinatario = destinatario
        self.__remitente = remitente
        self.__asunto = asunto
        self.prioridad = prioridad #1 = Urgente 0= normal

    def set_mensaje(self,nuevo_mensaje): #cambiar el nombre de la variable, es el mensaje que se va a escribir
        self.__mensaje = str(nuevo_mensaje)

    def set_destinatario(self, nuevo_destinatario):#Agregar más condiciones para que sea válido el destinatario
        if '@' in nuevo_destinatario:
            self.__destinatario = nuevo_destinatario
        else:
            raise ValueError('Ingresar una dirección de e-mail válida')
    
    def set_remitente(self,nuevo_remitente):#Lo mismo, fijemosnos si podemos agregar mas condiciones para que sea válido
        if '@' in nuevo_remitente:
            self.__remitente = nuevo_remitente
        else:
            raise ValueError('Ingresar una dirección de remitente válida')
        
    def set_asunto(self,nuevo_asunto):
        self.__asunto = str(nuevo_asunto)

    def __str__(self):
        información_mensaje = 'Información del mensaje:\n' + \
                            '------------------------\n' + \
                            'Remitente: ' + str(self.__remitente ) + '\n' + \
                            'Destinatario: ' + str(self.__destinatario) + '\n' + \
                            'Asunto: ' + str(self.__asunto) + '\n' + \
                            'Mensaje: ' + str(self.__mensaje) + '\n' 
        return información_mensaje

    def get_mensaje(self):
        return self.__mensaje

    def get_destinatario(self):
        return self.__destinatario
    
    def get_remitente(self):
        return self.__remitente
    
    def get_asunto(self):
        return self.__asunto
    
        

