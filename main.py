from servidor import ServidorCorreo
servidor = ServidorCorreo()
servidor.registrar_usuario('Juan', 'Perez', 'pass12345678', 'juancito@server.com')
servidor.registrar_usuario('Alberto', 'Diaz', 'contraseña123', 'alberdiaz@server.com')
usuario_juan = servidor.get_usuarios()['juancito@server.com'] 
raiz_juan = usuario_juan.raiz
raiz_juan.agregar_subcarpeta('Archivados')
carpeta_destino_archivados = raiz_juan.obtener_subcarpeta('Archivados')


servidor.enviar_mensaje(mensaje= 'Mensaje prueba de moverlo', destinatario='alberdiaz@server.com',remitente= 'juancito@server.com', asunto = 'prueba')


# Obtener la referencia al mensaje que está en la Bandeja de Salida
bandeja_salida_juan = usuario_juan.get_bandeja_salida()
mensaje_a_mover = bandeja_salida_juan.mensajes[0]

#mover mensaje
raiz_juan.mover_mensaje(mensaje_a_mover, carpeta_destino_archivados) 


# Verificar Origen (Debe tener 0)
bandeja_salida_final = usuario_juan.get_bandeja_salida()
print(f"Bandeja de Salida (ORIGEN) después del movimiento: {len(bandeja_salida_final.mensajes)}") 

# Verificar Destino (Debe tener 1)
carpeta_destino_final = usuario_juan.raiz.obtener_subcarpeta('Archivados')
print(f"Carpeta 'Archivados' (DESTINO) después del movimiento: {len(carpeta_destino_final.mensajes)}")