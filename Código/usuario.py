from carpeta import Carpeta

class Usuario:
    def __init__(self, nombre,apellido, contraseña,correo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contraseña = contraseña
        self.__correo = correo
        self.__bandeja_entrada = Carpeta('Bandeja de entrada')
        self.__bandeja_salida = Carpeta('Bandeja de salida')
        
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

    def guardar_mensaje_recibido(self,mensaje): #Guardamos un mensaje en la bandeja de entrada,usando el metodo de la clase Carpeta
       self.__bandeja_entrada.agregar_mensaje(mensaje)
    
    def guardar_mensaje_enviado(self,mensaje): #Guardamos un mensaje en la bandeja de salida,usando el metodo de la clase Carpeta
        self.__bandeja_salida.agregar_mensaje(mensaje)
    
    def get_bandeja_entrada(self):
       return self.__bandeja_entrada #Getter de la bandeja de entrada
    
    def get_bandeja_salida(self):
       return self.__bandeja_salida #Getter de la bandeja de salida