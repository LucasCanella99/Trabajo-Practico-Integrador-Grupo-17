from redservidores import RedServidores
from servidor import ServidorCorreo
from menu import Menu

#Creamos la red.Mapa topografico de los servidores
red_global = RedServidores()

#Creacion de instancias de servidor y como red le pasamos a todos la misma para que esten en el mismo mapa topografico
servidor_unab = ServidorCorreo('unab.edu.ar', red_global)
servidor_gmail = ServidorCorreo('gmail.com', red_global)
servidor_hotmail = ServidorCorreo('hotmail.com', red_global)
servidor_yahoo = ServidorCorreo('yahoo.com.ar', red_global)

#Diccionario de servidores para que funcione el menú. Clave nombre de dominio, valor objeto Servidor
servidores_en_uso = {'unab.edu.ar': servidor_unab,'gmail.com':servidor_gmail,'hotmail.com':servidor_hotmail,'yahoo.com.ar': servidor_yahoo}

#Creacion de aristas del grafo
red_global.agregar_conexion('unab.edu.ar','yahoo.com.ar')
red_global.agregar_conexion('unab.edu.ar','hotmail.com')
red_global.agregar_conexion('gmail.com','unab.edu.ar' )
red_global.agregar_conexion('yahoo.com.ar','gmail.com')

#Inicio de menu

menu = Menu(servidores_en_uso)

if __name__ == '__main__':
    menu.ejecucion()
