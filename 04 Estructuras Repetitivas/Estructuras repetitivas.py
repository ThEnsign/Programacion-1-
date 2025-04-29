#Práctico 4: Estructuras repetitivas
#Objetivo:
#Implementar ciclos para resolver problemas que requieran repetición de acciones.

#Actividades
#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un numero entero: "))
if numero == 0:
    cantidad = 1
else:
    numero = abs(numero)
    cantidad = 0
    while numero > 0:
        numero = numero // 10
        cantidad += 1

print("Cantidad de digitos:", cantidad)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores

inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
if inicio > fin:
    inicio, fin = fin, inicio
suma = 0
numero = inicio + 1
while numero < fin:
    suma += numero
    numero += 1
print("La suma de los números entre", inicio, "y", fin, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma= 0
numero= int(input("Ingrese un numero entero (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Ingrese otro numero (0 para terminar): "))
print("La suma total es:", suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numero_secreto= 4
intentos= 0
adivinado= False

while not adivinado:
    intento= int(input("Adivina el numero (entre 0 y 9): "))
    intentos+= 1
    if intento== numero_secreto:
        adivinado= True
        print("¡Correcto! Lo adivinaste en", intentos, "intento(s).")
    else:
        print("Incorrecto, intenta de nuevo.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

numero= 100

while numero>= 0:
    if numero% 2 == 0:
        print(numero)
    numero-= 1

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

limite= int(input("Ingrese un numero entero positivo: "))
suma= 0
contador= 0
while contador<= limite:
    suma+= contador
    contador+= 1

print("La suma de los numeros desde 0 hasta", limite, "es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el

total_numeros= 10
pares= 0
impares= 0
positivos= 0
negativos= 0
contador= 0

while contador< total_numeros:
    numero= int(input(f"Ingrese el numero {contador + 1}: "))
    if numero% 2 == 0:
        pares+= 1
    else:
        impares+= 1
    if numero> 0:
        positivos+= 1
    elif numero< 0:
        negativo += 1
    contador+= 1

print("Resumen:")
print("Cantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)

total_numeros= 10
suma= 0
contador= 0

while contador< total_numeros:
    numero= int(input(f"Ingrese el numero {contador + 1}: "))
    suma+= numero
    contador += 1
media= suma / total_numeros
print("La media de los", total_numeros, "numeros ingresados es:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero= int(input("Ingrese un numero entero: "))
invertido= 0

while numero!= 0:
    ultimo_digito= numero% 10
    invertido= invertido* 10 + ultimo_digito
    numero= numero // 10

print("Numero invertido:", invertido)
