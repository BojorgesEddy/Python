#captura de la correo electronico
email = input("Ingrese su correo electronico...\n")

#index divide la parte del cadena ingresada de email
#en este caso antes del arroba
#y se guarda en la variable nombre_usuario
nombre_usuario = email[:email.index('@')]

#index divide la parte del cadena ingresada
#en este caso despues del arroba, esto debido al +1, 
#ya que sin el +1 este tomaria el arroba y lo que le sigue
#y se guarda en la variable nombre_dominio
nombre_dominio = email[email.index('@')+1:]

#guardamos lo que se va a imprimir en una variable salida
salida = "Tu nombre de usuario es '{}' y el nombre de dominio es '{}'".format(nombre_usuario,nombre_dominio)

#imprime el mensaje
print(salida)