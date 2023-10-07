#Solicitamos informacion al usuario
nombre = input("Ingresa un nombre, puede ser el tuyo... ")
adjetivo = input("Cuéntame un adjetivo: ")
accion = input("dame un verbo en pasado para una acción en tu historia: ")
objeto = input("para finalizar, menciona un objeto que estará en tu historia: ")

#Metemos lo recolectado a la historio y lo guardamos en una variable
historia = f"Había una vez una persona llamada {nombre}. {nombre} era {adjetivo} y siempre soñaba con {accion} en su tiempo libre. Un día, mientras exploraba, encontró un {objeto} mágico que cambió su vida para siempre."

print("\nAquí está tu historia:")
#imprimimos la historia creada
print(historia)
