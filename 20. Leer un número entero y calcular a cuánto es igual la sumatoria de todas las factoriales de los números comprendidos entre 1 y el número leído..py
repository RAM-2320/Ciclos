n = int(input("Ingrese un número entero: "))
suma_factoriales = 0
for i in range(1, n + 1):
  factorial = 1
  for j in range(1, i + 1):
    factorial *= j
  suma_factoriales += factorial
print(f"La suma de las factoriales de los números de 1 a {n} es {suma_factoriales}")