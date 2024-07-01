numero = int(input("Ingrese un número entero de 3 dígitos: "))
if numero // 100 == 1 or numero % 10 == 1 or numero // 10 % 10 == 1:
    print("El número tiene el dígito 1.")
else:
    print("El número no tiene el dígito 1.")