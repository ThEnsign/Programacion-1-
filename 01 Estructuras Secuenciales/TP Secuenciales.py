#1
print(f"¡Hola mundo!")

#2
nombre= input("Ingrese su Nombre: ")
print(f"¡Hola {nombre}, bienvenido!")

#3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4
import math

radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area}")
print(f"El perímetro del círculo es: {perimetro}")

#5
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600

print(f"Equivale a {horas} horas.")

#6
numero = int(input("Ingrese un numero: "))

print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#7
numero1 = int(input("Ingrese el primer numero (distinto de 0): "))
numero2 = int(input("Ingrese el segundo numero (distinto de 0): "))

print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicacion:", numero1 * numero2)
print("Division:", numero1 / numero2)


#8
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)

print("IMC:", imc)

#9 celsius = float(input("Ingrese la temperatura en Celsius: "))

celsius = float(input("Ingrese la temperatura en Celsius: "))

print("Temperatura en Fahrenheit:", (9/5) * celsius + 32)


#10
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))

print("Promedio:", (numero1 + numero2 + numero3) / 3)