numero = int(input("Ingrese un número entero: "))

print("Tabla de multiplicar de", numero, ":")
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)