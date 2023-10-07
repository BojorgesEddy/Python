

frase = input("Ingresa el nombre de una organización o concepto: ")


palabras = frase.split()

# Tomar la primera letra de cada palabra y unirlas para crear el acrónimo
acronym = "".join(word[0].upper() for word in palabras)

# Imprimir el acrónimo
print(f"El acrónimo para '{frase}' es: {acronym}")

