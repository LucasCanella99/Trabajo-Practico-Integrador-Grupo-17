from servidor_correo import ServidorCorreo

class Interfaz:
    def __init__(self):
        self.__servidor = ServidorCorreo()

    def menu(self):
        while True:
            print('''Menú cliente de correo:  \n
                  1. Registrase: \n
                  ---------------\n
                  2. Enviar un mensaje: \n
                  ---------------\n
                  3. Mensajes de bandeja de entrada: \n
                  ---------------\n
                  4. Mensajes de bandeja de salida: \n
                  ---------------\n
                  5. Salir.''')
            
            opcion_elegida = int(input('Elige una opción: '))

            if opcion_elegida == 1:
                self.registrar_usuario()
            elif opcion_elegida == 2:
                self.enviar_mensaje()
            elif opcion_elegida == 3:
                self.listar_mensajes_entrada()
            elif opcion_elegida == 4:
                self.listar_mensajes_salida()
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
            print(f'Error al registrarse: {e}¡')# Si hay algun error aca lo muestra

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
            print(f'Error al enviar el mensaje: {e}¡') # Si hay algun error aca lo muestra
    
    def listar_mensajes_entrada(self):
        print('''Bandeja de entrada: \n
              ----------------------------''')
        try:
            correo = str(input('Ingrese su correo: '))
            self.__servidor.listar_mensajes_entrada(correo)
        except ValueError as e:
            print(f'Error al ingresar el correo: {e}')
    
    def listar_mensajes_salida(self):
        print('''Bandeja de salida: \n
              ----------------------------''')
        try:
            correo = str(input('Ingrese su correo: '))
            self.__servidor.listar_mensajes_salida(correo)
        except ValueError as e:
            print(f'Error al ingresar el correo: {e}')


