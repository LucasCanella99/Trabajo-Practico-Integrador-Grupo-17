from servidor import ServidorCorreo

class Menu:
    def __init__(self):
        self.__servidor = ServidorCorreo()

    def menu(self):
        while True:
            print('''Menú cliente de correo:  \n
                  1. Registrase: \n
                  ---------------\n
                  2. Enviar un mensaje: \n
                  ---------------\n
                  3. Recibir mensajes: \n
                  ---------------\n
                  4. Leer mensajes: \n
                  ---------------\n
                  5. Salir.''')
            
            opcion_elegida = int(input('Elige una opción: '))

            if opcion_elegida == 1:
                self.registrar_usuario()
            elif opcion_elegida == 2:
                self.enviar_mensaje()
            elif opcion_elegida == 3:
                self.recibir_mensajes()
            elif opcion_elegida == 4:
                self.listar_mensajes()
            elif opcion_elegida == 5:
                break
    
    def registrar_usuario(self):
        print('''Ingrese sus datos para registrarse: \n ' \
              --------------------------------------''')
        try:
            nombre = str(input('Ingrese su nombre: '))
            apellido = str(input('Ingrese su apellido: '))
            contraseña = str(input('Ingrese su contraseña: '))
            correo = str(input('Ingrese su nueva dirección de correo: '))
            self.__servidor.registrar_usuario(nombre,apellido,contraseña,correo)
            print('Se a registrado exitosamente¡')
        except ValueError as e:
            print('Error al registrarse: ' + str(e))# Si hay algun error aca lo muestra

    def enviar_mensaje(self):
        print('''Ingrese los siguientes datos para enviar un mensaje: \n ' \
              -------------------------------------------------------''')
        try:
            destinatario = str(input('Ingrese el correo del destinatario: '))
            remitente = str(input('Ingrese su correo: ')) # Acá tenemos que ver alguna manera de validar con la contraseña
            asunto = str(input('Ingrese el asunto del mensaje: '))
            mensaje = str(input('Ingrese su mensaje: '))

            self.__servidor.enviar_mensaje(mensaje,destinatario,remitente,asunto)

            print('Mensaje enviado con exito¡')
        except ValueError as e:
            print('Error al enviar el mensaje: ' + str(e) ) # Si hay algun error aca lo muestra
    
    def listar_mensajes(self):
        print('''Bandeja de entrada: \n
              ----------------------------''')
        try:
            correo = str(input('Ingrese su correo: '))
            tipo_de_bandeja = str(input('Ingrese el tipo de bandeja "entrada" o "salida": '))
            self.__servidor.listar_mensajes(correo,tipo_de_bandeja)     
        except ValueError as e:
            print('Error al ingresar el correo: ' + str(e))
    
    def recibir_mensajes(self):
        print('''Mensajes disponibles: \n ' \
              --------------------------------------''')
        try:
            correo = str(input('Ingrese su correo: '))
            mensajes = self.__servidor.recibir_mensaje(correo)
            print( mensajes )
        except ValueError as e:
            print('Error al ingresar el correo: ' + str(e))


