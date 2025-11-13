class Menu:
    def __init__(self,servidores_en_uso):
        self.__servidores_en_uso = servidores_en_uso

    def get_servidor(self,correo):
        try:
            dominio = correo.split('@')[-1].lower()
        except IndexError:
            raise ValueError('El correo debe contener @. Ingrese un correo válido.')
        
        if dominio in self.__servidores_en_uso:
            return self.__servidores_en_uso[dominio]
        else:
            raise ValueError('El correo no pertence a un servidor registrado.')
        
    def registrar_usuario(self):
        print('''Ingrese sus datos para registrarse: \n ' \
              --------------------------------------''')
        try:
            nombre = str(input('Ingrese su nombre: '))
            apellido = str(input('Ingrese su apellido: '))
            contraseña = str(input('Ingrese su contraseña: '))
            correo = str(input('Ingrese su nueva dirección de correo: '))
            servidor_asociado = self.get_servidor(correo)
            servidor_asociado.registrar_usuario(nombre,apellido,contraseña,correo)
            print('Se a registrado exitosamente¡')
        except ValueError as e:
            print('Error al registrarse: ' + str(e))

    def enviar_mensaje(self):
        print('''Ingrese los siguientes datos para enviar un mensaje: \n ' \
              -------------------------------------------------------''')
        try:
            destinatario = str(input('Ingrese el correo del destinatario: '))
            remitente = str(input('Ingrese su correo: ')) 
            asunto = str(input('Ingrese el asunto del mensaje: '))
            mensaje = str(input('Ingrese su mensaje: '))
            servidor_origen = self.get_servidor(remitente)

            servidor_origen.enviar_mensaje(mensaje,destinatario,remitente,asunto)

            print('Mensaje enviado con exito¡')
        except ValueError as e:
            print('Error al enviar el mensaje: ' + str(e) )

    def listar_mensajes(self):
        print('''Mensajes: \n
              ----------------------------''')
        try:
            correo = str(input('Ingrese su correo: '))
            carpeta = str(input('Ingrese el nombre de la carpeta solicitada: '))
            servidor_asociado = self.get_servidor(correo)
            
            servidor_asociado.listar_mensajes(correo,carpeta)     
        except ValueError as e:
            print('Error: ' + str(e))

    