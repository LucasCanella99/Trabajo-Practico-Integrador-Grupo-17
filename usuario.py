from carpeta import Carpeta

class Usuario:
    def __init__(self, nombre,apellido, contraseña,correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contraseña = contraseña
        self.__correo = correo
        #Atributos para arbol de carpetas
        self.raiz = Carpeta('Carpeta principal')
        #Subcarpetas predeterminadas
        self.raiz.agregar_subcarpeta('Bandeja de entrada')# Se crea en cada usuario una subcarpeta de la raiz, para mensajes de entrada
        self.raiz.agregar_subcarpeta('Bandeja de salida')# subcarpeta predeterminada para mensajes de salida
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor ):
        if valor.strip() == "":
         raise ValueError("El nombre del usuario no puede estar vacio")
        self.__nombre = valor
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,valor ):
        if  valor.strip() == "":
         raise ValueError("El apellido del usuario no puede estar vacio")
        self.__apellido = valor
    @property
    def contraseña(self):
        return self.__contraseña
    @contraseña.setter
    def contraseña(self,valor ):
       if len(valor) < 10:
         raise ValueError("Su contraseña debe tener al menos 10 caracteres")
       if valor.strip() == "":
          raise ValueError("La contraseña no puede estar vacia")
       self.__contraseña = valor
    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self,valor ):
       if not "@" in valor or not "." in valor:
         raise ValueError("ingrese un correo valido ")
       if valor.strip() == "":
          raise ValueError("Su correo no puede estar vacio")
       self.__correo = valor   

    def guardar_mensaje_recibido(self,mensaje): 
       bandeja_entrada = self.raiz.obtener_subcarpeta('Bandeja de entrada')
       if bandeja_entrada: #Una verificación extra que existe
          bandeja_entrada.agregar_mensaje(mensaje)#El metodo agregar_mensaje ya verifica si mensaje es una instancia de Mensaje
    
    def guardar_mensaje_enviado(self,mensaje): 
        bandeja_entrada = self.raiz.obtener_subcarpeta('Bandeja de salida')
        if bandeja_entrada:
            bandeja_entrada.agregar_mensaje(mensaje)
    
    def get_bandeja_entrada(self):
       return self.raiz.obtener_subcarpeta('Bandeja de entrada')
    
    def get_bandeja_salida(self):
       return self.raiz.obtener_subcarpeta('Bandeja de salida')
    #La razon de que estos metodos son simples es que estas carpetas por defecto ya estan en el dict de la raiz, lo que ahorra tiempo y es mucho mas eficiente