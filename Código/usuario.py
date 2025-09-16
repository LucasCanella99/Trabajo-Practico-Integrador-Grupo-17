class Usuario:
    def __init__(self, nombre,apellido, comtraseña,correo):
        self._nombre = nombre
        self._apellido = apellido
        self._contraseña = comtraseña
        self._correo = correo
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,valor ):
        if valor.strip() == "":
         raise ValueError("El nombre del usuario no puede estar vacio")
        self._nombre = valor
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self,valor ):
        if  valor.strip() == "":
         raise ValueError("El apellido del usuario no puede estar vacio")
        self._apellido = valor
    @property
    def contraseña(self):
        return self._contraseña
    @contraseña.setter
    def contraseña(self,valor ):
       if len(valor) < 10:
         raise ValueError("Su contraseña debe tener al menos 10 caracteres")
       if valor.strip() == "":
          raise ValueError("La contraseña no puede estar vacia")
       self._contraseña = valor
    @property
    def correo(self):
        return self._correo
    @correo.setter
    def correo(self,valor ):
       if not "@" in valor or not "." in valor:
         raise ValueError("ingrese un correo valido ")
       if valor.strip() == "":
          raise ValueError("Su correo no puede estar vacio")
       self._correo = valor   