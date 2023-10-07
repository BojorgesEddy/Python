# Solicitar nombre
nombre = input("¿Ingrese su nombre.. ")

# Verificar que el nombre sea de la a-z y A-Z y espacios
while not nombre.replace(" ", "").isalpha():
    print("Entrada incorrecta. Por favor, ingresa un nombre válido sin números ni caracteres especiales.")
    nombre = input("¿Ingrese su nombre.. ")


edad = input("Ingresa tu edad.. ")

# Verificar que la edad sea de 0-9
while not edad.isdigit() or int(edad) <= 0:
    print("Entrada incorrecta. Por favor, ingresa una edad válida como un número entero positivo.")
    edad = input("Ingresa tu edad.. ")


ciudad = input("Ingresa tu ciudad.. ")

# Verificar la validez de la ciudad (permitiendo letras y espacios)
while not ciudad.replace(" ", "").isalpha():
    print("Entrada incorrecta. Por favor, ingresa una ciudad válida sin números ni caracteres especiales.")
    ciudad = input("Ingresa tu ciudad.. ")


meta = input("Ingresa una meta personal.. ")

while not meta.replace(" ", "").isalpha():
    print("Entrada incorrecta. Por favor, ingresa una ciudad válida sin números ni caracteres especiales.")
    meta = input("Ingresa una meta personal.. ")

# Imprimir un resumen de la información ingresada
print("\nResumen de la información ingresada:")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Ciudad: {ciudad}")
print(f"Metas Personales: {meta}")
