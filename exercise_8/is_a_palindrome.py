# Solicitar al usuario que ingrese cinco palabras
palabras = []
for i in range(5):
    palabra = input(f"Ingrese la palabra #{i + 1}: ")
    palabras.append(palabra)

# Verificar si alguna de las palabras es un palíndromo
palindromos = []
for palabra in palabras:
    if palabra == palabra[::-1]:  # Comprobar si la palabra es igual al revés
        palindromos.append(palabra)#agrega un elemento a la lista palindromos

# Imprimir los resultados
if palindromos:
    print(f"Las siguientes palabras son palíndromos: {', '.join(palindromos)}")#se ingresa las palabras de la lista palindromos como cadena de texto separados por una coma y un espacio
else:
    print("Ninguna de las palabras que ingresaste es un palíndromo.")
