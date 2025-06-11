#actividad 1) escribir un programa que solicite la edad del usuario. si el usuario es mayor de 18 anos,debera mostrar un mensaje en pantalla que diga “es mayor de edad”.

edad = int(input("ingrese su edad: "))
if edad > 18:
    print("es mayor de edad")

#actividad 2) escribir un programa que solicite su nota al usuario. si la nota es mayor o igual a 6, debera mostrar por pantalla un mensaje que diga “aprobado”; en caso contrario debera mostrar el mensaje “desaprobado”.

nota = float(input("ingrese su nota: "))
if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")

#actividad 3) escribir un programa que permita ingresar solo numeros pares. si el usuario ingresa un numero par, imprimir por en pantalla el mensaje "ha ingresado un numero par"; en caso contrario, imprimir por pantalla "por favor, ingrese un numero par". nota: investigar el uso del operador de modulo (%) en python para evaluar si un numero es par o impar.

numero = int(input("ingrese un numero: "))
if numero % 2 == 0:
    print("ha ingresado un numero par")
else:
    print("por favor, ingrese un numero par")

#actividad 4) escribir un programa que solicite al usuario su edad e imprima por pantalla a cual de las siguientes categorias pertenece:
#● nino/a: menor de 12 anos.
#● adolescente: mayor o igual que 12 anos y menor que 18 anos.
#● adulto/a joven: mayor o igual que 18 anos y menor que 30 anos.
#● adulto/a: mayor o igual que 30 anos

edad = int(input("ingrese su edad: "))

if edad < 12:
    print("nino/a")
elif edad >= 12 and edad < 18:
    print("adolescente")
elif edad >= 18 and edad < 30:
    print("adulto joven")
else:
    print("adulto")

#actividad 5) escribir un programa que permita introducir contrasenas de entre 8 y 14 caracteres (incluyendo 8 y 14). si el usuario ingresa una contrasena de longitud adecuada, imprimir por en pantalla el mensaje "ha ingresado una contrasena correcta"; en caso contrario, imprimir por pantalla "por favor, ingrese una contrasena de entre 8 y 14 caracteres". nota: investigue el uso de la funcion len() en python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string

contrasena = input("ingrese una contrasena: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("ha ingresado una contrasena correcta")
else:
    print("por favor, ingrese una contrasena de entre 8 y 14 caracteres")

#actividad 6) 

import random
from statistics import mean, median, mode

#paso 1: generar y mostrar la lista
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print("lista generada:")
print(numeros_aleatorios)

#paso 2: calcular media, mediana y moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("\nmedia:", media)
print("mediana:", mediana)
print("moda:", moda)

#paso 3: evaluar tipo de sesgo
if media > mediana and mediana > moda:
    print("\nresultado: sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("\nresultado: sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("\nresultado: sin sesgo")
else:
    print("\nresultado: no se puede determinar un sesgo claro")

#actividad 7) escribir un programa que solicite una frase o palabra al usuario. si el string ingresado termina con vocal, anadir un signo de exclamacion al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingreso el usuario e imprimirlo por pantalla.

frase = input("ingrese una frase o palabra: ")

#verificon de una vocal (minuscula o mayuscula)
if frase.lower().endswith(('a', 'e', 'i', 'o', 'u')):
    frase += "!"
    
print(frase)

#actividad 8) escribir un programa que solicite al usuario que ingrese su nombre y el numero 1, 2 o 3 dependiendo de la opcion que desee:
#1. si quiere su nombre en mayusculas. por ejemplo: pedro.
#2. si quiere su nombre en minusculas. por ejemplo: pedro.
#3. si quiere su nombre con la primera letra mayuscula. por ejemplo: pedro. 
#el programa debe transformar el nombre ingresado de acuerdo a la opcion seleccionada por el usuario e imprimir el resultado por pantalla. nota: investigue uso de las funciones upper(), lower() y title() de python para convertir entre mayusculas y minusculas.

#solicitar datos al usuario
nombre = input("ingrese su nombre: ")
opcion = input("ingrese una opcion (1 = mayusculas, 2 = minusculas, 3 = primera letra mayuscula): ")

#aplicar la transformacion segun la opcion
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("opcion no valida.")

#actividad 9) escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorias segun la escala de richter e imprima el resultado por pantalla:
#● menor que 3: "muy leve" (imperceptible).
#● mayor o igual que 3 y menor que 4: "leve" (ligeramente perceptible).
#● mayor o igual que 4 y menor que 5: "moderado" (sentido por personas, pero generalmente no causa danos).
#● mayor o igual que 5 y menor que 6: "fuerte" (puede causar danos en estructuras debiles).
#● mayor o igual que 6 y menor que 7: "muy fuerte" (puede causar danos significativos).
#● mayor o igual que 7: "extremo" (puede causar graves danos a gran escala).

magnitud = float(input("ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("muy leve (imperceptible)")
elif magnitud < 4:
    print("leve (ligeramente perceptible)")
elif magnitud < 5:
    print("moderado (sentido por personas, pero no causa danos)")
elif magnitud < 6:
    print("fuerte (puede causar danos en estructuras debiles)")
elif magnitud < 7:
    print("muy fuerte (puede causar danos significativos)")
else:
    print("extremo (puede causar graves danos a gran escala)")

#actividad 10) escribir un programa que pregunte al usuario en cual hemisferio se encuentra (n/s), que mes del ano es y que dia es. el programa debera utilizar esa informacion para imprimir por pantalla si el usuario se encuentra en otono, invierno, primavera o verano.

hemisferio = input("ingrese su hemisferio (n/s): ").upper()
mes = int(input("ingrese el mes (numero del 1 al 12): "))
dia = int(input("ingrese el dia: "))

#convertimos la fecha en formato mmdd para comparar.
fecha = mes * 100 + dia

if 1221 <= fecha <= 1231 or 101 <= fecha <= 320:
    estacion = "invierno" if hemisferio == "n" else "verano"
elif 321 <= fecha <= 620:
    estacion = "primavera" if hemisferio == "n" else "otono"
elif 621 <= fecha <= 920:
    estacion = "verano" if hemisferio == "n" else "invierno"
else:
    estacion = "otono" if hemisferio == "n" else "primavera"

print("la estacion actual es:", estacion)
