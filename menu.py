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
    
    def crear_subcarpeta_principal(self):
        print('''Ingrese los siguientes datos para crear una subcarpeta principal: \n ' \
              -------------------------------------------------------''')
        try:
            correo = str(input('Ingrese su correo: '))
            carpeta = str(input('Ingrese el nombre de la carpeta a crear: '))
            servidor_asociado = self.get_servidor(correo)
            servidor_asociado.crear_subcarpeta_principal(correo,carpeta)
        except ValueError as e:
            print('Error: ' + str(e))

    def crear_subcarpeta_anidada(self):
        print('''Ingrese los siguientes datos para crear una subcarpeta anidada: \n ' \
              -------------------------------------------------------''')
        try:
            correo = str(input('Ingrese su correo: '))
            carpeta = str(input('Ingrese el nombre de la carpeta a crear: '))
            carpeta_padre= str(input('Ingrese el nombre de la carpeta en la que quiera crear la subcarpeta '))
            servidor_asociado = self.get_servidor(correo)
            servidor_asociado.crear_subcarpeta_anidada(correo,carpeta,carpeta_padre)
        except ValueError as e:
            print('Error: ' + str(e))

    def mover_mensaje(self):
        print('''Ingrese los siguientes datos para mover un mensaje por su asunto: \n ' \
              -------------------------------------------------------''')
        try:
            correo = input('Ingrese su correo: ')
            asunto_buscado = input('Ingrese el asunto del mensaje a mover: ')
            nombre_carpeta_destino = input('Ingrese el nombre de la carpeta de destino: ')
            servidor_asociado = self.get_servidor(correo)
            servidor_asociado.mover_mensaje(correo,asunto_buscado,nombre_carpeta_destino)
        except ValueError as e:
            print('Error: ' + str(e))

    def contador_mensajes(self):
        print('''Contador mensajes de bandeja de entrada: \n ' \
              -------------------------------------------------------''')
        try:
            correo = str(input('Ingrese su correo: '))
            servidor_asociado = self.get_servidor(correo)
            resultado = servidor_asociado.recibir_mensaje(correo)
            print(resultado)
        except ValueError as e:
            print('Error: ' + str(e))

    def ejecucion(self):
        while True:
            print('''\n------------------------------------\nMenú cliente de correo:  \n
                  1. Registrarse: \n
                  ---------------\n
                  2. Enviar un mensaje: \n
                  ---------------\n
                  3. Contador de mensajes: \n
                  ---------------\n
                  4. Ver mensajes por carpeta: \n
                  ---------------\n
                  5. Crear subcarpeta principal: \n
                  ---------------\n
                  6. Crear una subcarpeta de otra carpeta: \n
                  ---------------\n
                  7. Mover mensaje:\n
                  ---------------\n
                  8. Salir.\n
                  ------------------------------------''')

            try:
                opcion_elegida = int(input('Elegi una opción: '))
            except ValueError:
                print('Opción inválida. Ingrese un número.')
                continue

            if opcion_elegida == 1:
                self.registrar_usuario()
            elif opcion_elegida == 2:
                self.enviar_mensaje()
            elif opcion_elegida == 3:
                self.contador_mensajes()
            elif opcion_elegida == 4:
                self.listar_mensajes()
            elif opcion_elegida == 5:
                self.crear_subcarpeta_principal()
            elif opcion_elegida == 6:
                self.crear_subcarpeta_anidada()
            elif opcion_elegida == 7:
                self.mover_mensaje()
            elif opcion_elegida == 8:
                print('\n Saliendo...')
                break
            else:
                print('Opción invalida. Intente de nuevo.')