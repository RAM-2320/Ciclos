numero = int(input("Ingrese un número entero de dos dígitos: "))
digito1 = numero // 10
digito2 = numero % 10
for i in range(digito1 + 1, digito2):
    print(i)