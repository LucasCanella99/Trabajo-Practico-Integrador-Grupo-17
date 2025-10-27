from mensaje import Mensaje

class Carpeta:
    def __init__(self,nombre):
        self.nombre = nombre
        self.mensajes = []
        self.subcarpetas = {}

    def agregar_subcarpeta(self,nombre):
        if nombre in self.subcarpetas:
            raise ValueError('La carpeta ' + str(nombre) +' ya existe!')

        nueva_subcarpeta = Carpeta(nombre)
        self.subcarpetas[nombre] = nueva_subcarpeta

        return nueva_subcarpeta
    
    def obtener_subcarpeta(self,nombre):
        subcarpeta_a_obtener = self.subcarpetas.get(nombre)
        return subcarpeta_a_obtener
    
    def buscar_mensajes(self,criterio_de_busqueda): #Hace una busqueda recursiva, primero en la raiz, y luego recursivamente en las subcarpetas
                                                    # y agrega todos los mensajes coincidentes en resultados y finalmente lo retorna
        resultados = []                             
        for mensaje in self.mensajes:
            if criterio_de_busqueda in  mensaje.asunto or criterio_de_busqueda in mensaje.remitente:
                resultados.append(mensaje)

        for subcarpeta in self.subcarpetas.values():
            busqueda_recursiva = subcarpeta.buscar_mensajes(criterio_de_busqueda)
            resultados.extend(busqueda_recursiva)

        return resultados
    
    #Metodos auxiliares para hacer el mover mensaje

    def agregar_mensaje(self,mensaje):
        if isinstance(mensaje,Mensaje):
            self.mensajes.append(mensaje)
        else:
            print('Solo se pueden agregar mensajes de tipo Mensaje')
            return
        
    def eliminar_mensaje(self,mensaje):
        if not isinstance(mensaje,Mensaje):
            raise TypeError('Solo se pueden eliminar mensajes de tipo Mensaje')
            
        try:
            self.mensajes.remove(mensaje)
        except ValueError:
            print('No se a encontrado el mensaje a eliminar')

    def obtener_carpeta(self,mensaje):
        if mensaje in self.mensajes:
            return self #Devuelve la carpeta donde esta el mensaje,si es la primera(raiz)
        
        for subcarpeta in self.subcarpetas.values():#Busca en las subcarpetas recursivamente
            carpeta_actual = subcarpeta.obtener_carpeta(mensaje)
            if carpeta_actual is not None:
                return carpeta_actual #Si lo encontro retorna la carpeta de origen 
        return None#No lo encontro en ninguna subcarpeta    
    
    #Damos por entendido que el usuario introduce el mensaje que quiere mover,ahi si aplicamos recursión para encontrar la subcarpeta.Origen
    #Pero tambien damos por entendido que el usuario ya sabe a donde quiere mover el mensaje y el mismo da el destino.

    def mover_mensaje(self,mensaje,destino):
        if not isinstance(destino,Carpeta):
            raise TypeError('La carpeta de destino debe ser un objeto tipo Carpeta')
            
        carpeta_origen = self.obtener_carpeta(mensaje)
        if carpeta_origen is None:
            raise ValueError('No se encontró el mensaje a mover')
        carpeta_origen.eliminar_mensaje(mensaje) #Eliminamos el mensaje de la carpeta de origen
        destino.agregar_mensaje(mensaje)#Lo agregamos en la carpeta de destino proporcionada por el usuario
        print ('El mensaje se ha movido de la carpeta ' + str(carpeta_origen.nombre) + ' a la carpeta ' + str(destino.nombre) + ' con exito!')
        return True

    def obtener_carpeta_padre(self,carpeta_padre): #creamos este metodo para obtener la carpeta padre
        if carpeta_padre in self.subcarpetas:
            return self.subcarpetas[carpeta_padre]     #Complejidad 0(1) ya que es busqueda en diccionario
        
        for subcarpeta in self.subcarpetas.values(): #Busqueda recursiva en subcarpetas, complejidad 0(n) ya que depende de la cant. de subcarpetas.
            resultado =  subcarpeta.obtener_carpeta_padre(carpeta_padre)

            if resultado is not None:
                return resultado #se encontró y se devuelve la ubicación
        
        return None #no se encontró nada

        
            