num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

for i in range(num1, num2 + 1):
    if i % 10 == 4:
        print(i)