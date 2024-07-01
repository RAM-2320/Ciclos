suma = 0
cantidad = 0
numero = int(input("Ingrese un número (0 para terminar): "))
while numero != 0:
    if numero % 10 == 5:
        suma += numero
        cantidad += 1
    numero = int(input("Ingrese un número (0 para terminar): "))
if cantidad > 0:
    promedio = suma / cantidad
    print(f"El promedio de los números terminados en 5 es: {promedio}")
else:
    print("No se ingresaron números terminados en 5")