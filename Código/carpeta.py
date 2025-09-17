from mensaje import Mensaje

class Carpeta:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []  # Lista para guardar __mensajes

    def set_nombre(self, nombre_carpeta):
        if isinstance(nombre_carpeta,str):
            self.__nombre = nombre_carpeta
        else:
            raise ValueError('Introduce un nombre válido de carpeta')
    
    def get_nombre(self): 
        return self.__nombre

    def agregar_mensaje(self, mensaje):
        if isinstance(mensaje,Mensaje):
            self.__mensajes.append(mensaje) #Agrega un mensaje a la carpeta
        else:
            raise ValueError('Solo se pueden agregar objetos de la clase Mensaje a Carpeta')

    def eliminar_mensaje(self, mensaje_id):
        self.__mensajes = [m for m in self.__mensajes if m.id != mensaje_id] #Eliminar un mensaje por su ID

    def lista_de_mensajes(self):
        return self.__mensajes.copy() #Devuelve la lista de __mensajes
                                      # Le puse .copy() para que devuelva una copia de la lista de mensajes y no se modifique por accidente los mensjaes dentro de la carpeta

    def buscar_mensaje(self, criterio):
        return [m for m in self.__mensajes if criterio(m)] #función que recibe un mensaje y devuelve True o False.

    def __str__(self):
        return f"Carpeta '{self.__nombre}' con {len(self.__mensajes)} mensajes"