# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


# Ejercicio 2
def saludar_usuario(nombre):
    return "Hola " + nombre

nombre = input("Ingresa tu nombre: ")
print(saludar_usuario(nombre))


# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    return "Soy " + nombre + " " + apellido + ", tengo " + edad + " años y vivo en " + residencia

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))


# Ejercicio 4
def calcular_area_circulo(radio):
    return 3.14 * radio * radio

def calcular_perimetro_circulo(radio):
    return 2 * 3.14 * radio

radio = float(input("Ingresa el radio del circulo: "))
print("Area:", calcular_area_circulo(radio))
print("Perimetro:", calcular_perimetro_circulo(radio))


# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresa los segundos: "))
print("Horas:", segundos_a_horas(segundos))


# Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero = int(input("Ingresa un numero: "))
tabla_multiplicar(numero)


# Ejercicio 7
def operaciones_basicas(a, b):
    print("Suma:", a + b)
    print("Resta:", a - b)
    print("Multiplicacion:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("No se puede dividir por cero")

a = float(input("Numero 1: "))
b = float(input("Numero 2: "))
operaciones_basicas(a, b)


# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura * altura)

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))
print("Tu IMC es:", calcular_imc(peso, altura))


# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius = float(input("Temperatura en Celsius: "))
print("En Fahrenheit:", celsius_a_fahrenheit(celsius))


# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Numero 1: "))
b = float(input("Numero 2: "))
c = float(input("Numero 3: "))
print("Promedio:", calcular_promedio(a, b, c))
