class Mensaje:
    def __init__(self,mensaje,destinatario,remitente,asunto,prioridad=0):
        self._mensaje = mensaje
        self._destinatario = destinatario
        self._remitente = remitente
        self._asunto = asunto
        self.prioridad = prioridad #Urgente = 0 y normal = 1

    def set_mensaje(self,nuevo_mensaje): #cambiar el nombre de la variable, es el mensaje que se va a escribir
        self._mensaje = str(nuevo_mensaje)

    def set_destinatario(self, nuevo_destinatario):#Agregar más condiciones para que sea válido el destinatario
        if '@' in nuevo_destinatario:
            self.__destinatario = nuevo_destinatario
        else:
            raise ValueError('Ingresar una dirección de e-mail válida')
    
    def set_remitente(self,nuevo_remitente):#Lo mismo, fijemosnos si podemos agregar mas condiciones para que sea válido
        if '@' in nuevo_remitente:
            self._remitente = nuevo_remitente
        else:
            raise ValueError('Ingresar una dirección de remitente válida')
        
    def set_asunto(self,nuevo_asunto):
        self.__asunto = str(nuevo_asunto)

    def __str__(self):
        información_mensaje = 'Información del mensaje:\n' + \
                            '------------------------\n' + \
                            'Remitente: ' + str(self._remitente ) + '\n' + \
                            'Destinatario: ' + str(self._destinatario) + '\n' + \
                            'Asunto: ' + str(self._asunto) + '\n' + \
                            'Mensaje: ' + str(self._mensaje) + '\n' 
        return información_mensaje

    def get_mensaje(self):
        return self._mensaje

    def get_destinatario(self):
        return self._destinatario
    
    def get_remitente(self):
        return self._remitente
    
    def get_asunto(self):
        return self._asunto
    
        

