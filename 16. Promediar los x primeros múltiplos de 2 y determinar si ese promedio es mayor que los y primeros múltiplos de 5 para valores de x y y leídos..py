x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

promedio_multiplos_2 = sum(range(2, 2*x + 1, 2)) / x
promedio_multiplos_5 = sum(range(5, 5*y + 1, 5)) / y

if promedio_multiplos_2 > promedio_multiplos_5:
    print(f"El promedio de los {x} primeros múltiplos de 2 es mayor")
else:
    print(f"El promedio de los {x} primeros múltiplos de 2 no es mayor")
