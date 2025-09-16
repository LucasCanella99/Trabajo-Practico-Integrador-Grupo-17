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
                self.