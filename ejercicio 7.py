"""7. Descuento en la tienda
Enunciado: Una tienda ofrece descuentos según el monto de la compra. Si es menor a $50, no hay descuento. Si está entre $50 y $100,
hay un 5% de descuento. Si es mayor a $100, el descuento es del 10%. Pide el total de la compra y muestra el total a pagar.
Conceptos: Variables, if-elif-else, cálculos de porcentajes."""

# Pedir el total de la compra
total = float(input("Total de la compra: "))

# Calcular el descuento según el total
if total < 50:
    descuento = 0
elif total <= 100:
    descuento = total * 0.05
else:
    descuento = total * 0.10

# Calcular el total a pagar
a_pagar = total - descuento

# Mostrar el descuento y el total a pagar
print("Descuento: ", descuento)
print("Total a pagar:" , a_pagar )