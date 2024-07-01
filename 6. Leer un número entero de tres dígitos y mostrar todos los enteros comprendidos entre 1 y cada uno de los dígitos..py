numero = int(input("Ingrese un número de tres dígitos: "))
centenas = numero // 100
decenas = (numero % 100) // 10
unidades = numero % 10

for i in range(1, centenas + 1):
    print(f"Centena {i}")
for i in range(1, decenas + 1):
    print(f"Decena {i}")
for i in range(1, unidades + 1):
    print(f"Unidad {i}")