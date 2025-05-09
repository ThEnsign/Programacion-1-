# Práctico 5: Listas en Python

#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiplos_de_4= list(range(4, 101, 4))
print("1) Multiplos de 4:", multiplos_de_4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

gustos = ["boxeo", "milanesas con pure", "videojuegos", "musica", "programar"]
print("2) Gustos personales:", gustos)

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

lista_vacia= []
lista_vacia.append("perro")
lista_vacia.append("gato")
lista_vacia.append("leon")
print("3) Lista creada agregando elementos:", lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

animales= ["perro", "gato", "conejo", "pajaro"]
animales[0]= "leon"
animales[-1]= "oso"
print("4) Lista animales modificada:", animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros= [8, 15, 3, 22, 7]
numeros.remove(max(numeros)) 
print("5) Lista sin el número mayor:", numeros)

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

numeros= list(range(10, 31, 5)) # [10, 15, 20, 25, 30]
print("6) Primeros dos valores:", numeros[0:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos= ["raptor", "lamborghini", "camaro", "ferrari"]
autos[1:3] = ["roll royce", "tesla"]
print("7) Lista autos modificada:", autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

dobles= []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista con numeros dobles:", dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes: compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

compras= [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a)Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")
#b)Reemplazar "fideos" por "tallarines"
compras[1][1]= "tallarines"
#c)Eliminar "pan" del primer cliente
compras[0].remove("pan")
#d)Imprimir lista final
print("9) Lista de compras modificada:", compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada= [
    15,                      
    [25.5, 57.9],           
    [30.6, False]           
]
print("10) Lista anidada final:", lista_anidada)
