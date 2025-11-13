import collections

class RedServidores:
    def __init__(self):
        self.__conexiones = {} #La lista de adyacencia contiene los nodos y sus aristas. 

    def agregar_servidor(self,dominio): #Si no existe el servidor (nodo) lo agregamos a la red.
        if dominio not in self.__conexiones:
            self.__conexiones[dominio] = set() # El set se crea como dominio y conexiones con otros dominios
    
    def agregar_conexion(self,origen,destino): #Aca agregamos las aristas dirigidas
        if origen not in self.__conexiones:
            raise ValueError('El servidor de origen: ' + str(origen) + 'no está registrado.')
        if destino not in self.__conexiones:
            raise ValueError('El servidor de destino: ' + str(destino) + 'no está registrado.')
        #Agregamos la arista si pasó la verificación previa

        self.__conexiones[origen].add(destino) #Agregamos el servidor con su conexion a la lista de adyacencias

    def encontrar_ruta(self,origen,destino):#BFS
        if origen not in self.__conexiones or destino not in self.__conexiones:
            raise ValueError('El dominio del remitente o el dominio del receptor no coinciden con los dominios registrados.')
        if origen == destino:
            return [origen] #Si se envia un mensaje en el mismo dominio se retorna la ruta misma en si.
        
        cola = collections.deque([(origen,[origen])]) # Creamos la cola donde cada elemento es una tupla, que contiene dominio con su historial de ruta

        visitados = {origen} #Creamos un set, donde se guardan todos los dominios que ya fueron visitados para evitar un bucle infinito

        while cola: #Mientras haya nodos en la cola
            (nodo_actual,ruta) = cola.popleft() # Sacamos el primer nodo de la cola actual

            for conexion in self.__conexiones[nodo_actual]: #iteramos sobre las conexiones de ese nodo
                if conexion ==  destino:
                    return ruta + [destino] #Si econtramos el destino retornamos la ruta desde el origen hasta el destino
                
                if conexion not in visitados:
                    visitados.add(conexion) # Se siguio la iteracion y se agrego al set de visitados. Para evitar un bucle infinito.

                    nueva_ruta = ruta + [conexion] #nueva ruta 
                    cola.append((conexion,nueva_ruta)) # Se agrega el nuevo dominio a la cola como un nodo con su ruta

            # Esto se hace con cada conexion de la ruta del nodo, hasta que no quedan mas conexiones y despues se hace lo mismo con cada nuevo nodo
            #Osea cada conexion del nodo anterior. Y luego se itera sobre cada conexion de los nuevos nodos que fueron agregandose a la tupla. Asi
            # se asegura el algoritmo de BFS de recorrer por nivel toda la lista de adyacencia y retorna la ruta con menos nodos (dominios en nuestro caso)
            # intermedios.

        return 'Ruta no encontrada, no hay una ruta definida entre los servidores de origen y destino'    




