# Practico 6: estructuras de datos complejas

# Ejercicio 1: diccionario de precios de frutas
precios_frutas = {
    'Banana': 1200,
    'Anana': 2500,
    'Melon': 3000,
    'Uva': 1450
}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2: modificacion de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

# Ejercicio 3: frutas con precio mayor a 2000
frutas_caras = []
for fruta, precio in precios_frutas.items():
    if precio > 2000:
        frutas_caras.append(fruta)

# Ejercicio 4: agenda de contactos
contactos = {}
contactos['Juan'] = '123456'
contactos['Ana'] = '987654'
contactos['Luis'] = '789123'
contactos['Maria'] = '321789'
contactos['Tomas'] = '456987'
nombre_consulta = 'Juan'
numero_asociado = contactos.get(nombre_consulta, 'No existe')
print('Numero asociado a', nombre_consulta + ':', numero_asociado)

# Ejercicio 5: contar palabras unicas y sus repeticiones
frase = 'hola mundo hola'
palabras = frase.split()
unicas = set(palabras)
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print('Palabras unicas:', unicas)
print('Recuento:', recuento)

# Ejercicio 6: promedios de notas
alumnos = {
    'Sofia': (10, 9, 8),
    'Luis': (6, 7, 7)
}
promedios = {}
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    promedios[alumno] = promedio
print('Promedios:', promedios)

# Ejercicio 7: uso de conjuntos
parcial1 = {'Ana', 'Luis', 'Sofia', 'Juan'}
parcial2 = {'Sofia', 'Pedro', 'Juan'}
ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
solo_parcial1 = parcial1 - parcial2
print('Ambos parciales:', ambos)
print('Solo uno:', solo_uno)
print('Solo parcial 1:', solo_parcial1)

# Ejercicio 8: stock de productos
stock = {
    'lapiz': 10,
    'cuaderno': 5
}
producto = 'lapiz'
unidades = 3
if producto in stock:
    stock[producto] += unidades
else:
    stock[producto] = unidades
print('Stock actualizado:', stock)

# Ejercicio 9: agenda con claves compuestas
agenda = {
    ('lunes', '10:00'): 'Reunion',
    ('martes', '15:00'): 'Clase de ingles'
}
consulta = agenda.get(('lunes', '10:00'), 'No hay actividad')
print('Actividad:', consulta)

# Ejercicio 10: diccionario invertido de paises y capitales
original = {
    'Argentina': 'Buenos Aires',
    'Chile': 'Santiago'
}
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais
print('Diccionario invertido:', invertido)
