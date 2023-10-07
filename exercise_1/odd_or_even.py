# Bojorges Romero Eddy Abrham 

# Pide al usuario un numero del 1 al 1000 y lo pasa a int
numero = int(input("Por favor, ingresa un número entre 1 y 1000: "))

# Verificar que el numero este entre el rango
if 1 <= numero <= 1000:
    #hace el calculo si el residuo es cero es par e imprime
    #la f-strings se utiliza cuando se tiene variables dentro de lo que se va a imprimir
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
    else:
        #de lo contrario imprime impar
        print(f"{numero} es un número impar.")
else:
    #de un numero entre el rango manda este mensaje
    print("Por favor, ingresa un número válido dentro del rango de 1 a 1000.")

