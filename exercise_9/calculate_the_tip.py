# Solicitar la factura total
factura_total = float(input("Cuál es la factura total de hoy, por favor? $"))

# # Calcular propinas
# round se encarfa de redondear datos numericos
propina_18 = round(factura_total * 0.18)
propina_20 = round(factura_total * 0.20)
propina_25 = round(factura_total * 0.25)

# Mostrar propinas y total con propina
print(f"La propina del 18% es de ${propina_18}, lo que eleva el total a ${factura_total + propina_18}")
print(f"La propina del 20% es de ${propina_20}, lo que eleva el total a ${factura_total + propina_20}")
print(f"La propina del 25% es de ${propina_25}, lo que eleva el total a ${factura_total + propina_25}")



# Preguntar la cantidad de personas involucradas
personas_involucradas = int(input("Cuántas personas están involucradas? "))

# Preguntar si quieren dividir de manera desigual
dividir_desigual = input("Quieres dividir de manera desigual? (si/no) ").lower()

# Dividir equitativamente o de manera desigual
if dividir_desigual == "si":
    factura_total = factura_total + propina_18
    porcentaje_pago = float(input("Por favor, ingrese el porcentaje del pago de la primera persona (por ejemplo, 70): ")) / 100
    total_persona_1 = round(factura_total * porcentaje_pago)
    total_persona_2 = round(factura_total * (1 - porcentaje_pago))
    print(f"La primera persona paga ${total_persona_1} y los demas pagan ${(total_persona_2/(personas_involucradas-1)):.2f}")#:.2f indica que solo mostrara los dos digitoxs despues del punto decimal
else:
    total_por_persona = round((factura_total + propina_18) / personas_involucradas, 2)
    print(f"Cada persona debe pagar ${total_por_persona}")
