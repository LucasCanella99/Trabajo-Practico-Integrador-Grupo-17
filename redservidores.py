import collections

class RedServidores:
    def __init__(self):
        self.__conexiones = {} #La lista de adyacencia contiene los nodos y sus aristas. 

    def agregar_servidor(self,dominio): #Si no existe el servidor (nodo) lo agregamos a la red.
        if dominio not in self.__conexiones:
            self.__conexiones[dominio] = set()
    
    def agregar_conexion(self,origen,destino): #Aca agregamos las aristas dirigidas
        if origen not in self.__conexiones:
            raise ValueError('El servidor de origen: ' + str(origen) + 'no está registrado.')
        if destino not in self.__conexiones:
            raise ValueError('El servidor de destino: ' + str(origen) + 'no está registrado.')
        #Agregamos la arista si pasó la verificación previa

        self.__conexiones[origen].add(destino)
        

