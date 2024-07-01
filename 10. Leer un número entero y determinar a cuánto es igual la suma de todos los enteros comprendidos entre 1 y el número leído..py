numero = int(input("Ingrese un número entero: "))
suma = 0
for i in range(1, numero + 1):
    suma += i
print("La suma de los enteros comprendidos entre 1 y", numero, "es:", suma)