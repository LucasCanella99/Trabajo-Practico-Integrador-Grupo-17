class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []  # Lista para guardar mensajes

    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje) #Agrega un mensaje a la carpeta

    def eliminar_mensaje(self, mensaje_id):
        self.mensajes = [m for m in self.mensajes if m.id != mensaje_id] #Eliminar un mensaje por su ID

    def listar_mensajes(self):
        return self.mensajes #Devuelve la lista de mensajes

    def buscar_mensaje(self, criterio):
        return [m for m in self.mensajes if criterio(m)] #función que recibe un mensaje y devuelve True o False.

    def __str__(self):
        return f"Carpeta '{self.nombre}' con {len(self.mensajes)} mensajes"