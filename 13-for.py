# for bucles
lenguajes = ["Python", "JavaScript", "Java", "C++", "Ruby"]
for lenguaje in lenguajes:
    print(lenguaje)
print("Fin del bucle")


# for con range
for i in range(5):
    print(i)
print("Fin del bucle con range")
for i in range(2, 10, 2):
    print(i)
print("Fin del bucle con range y paso")
# for con else
for i in range(3):
    print(i)
else:
    print("Bucle terminado")
# for anidado
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
print("Fin del bucle anidado")
# for con break
for i in range(5):
    if i == 3:
        break
    print(i)
print("Bucle terminado con break")
# for con continue
for i in range(5):
    if i == 2:
        continue
    print(i)
print("Bucle terminado con continue")
# for con pass
for i in range(5):
    if i == 2:
        pass
    print(i)
print("Bucle terminado con pass")
# for con listas y diccionarios
nombres = ["Ana", "Luis", "Carlos"]
edades = {"Ana": 25, "Luis": 30, "Carlos": 35}
for nombre in nombres:
    print(nombre)
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")
print("Fin del bucle con listas y diccionarios")
# for con cadenas
cadena = "Hola"
for letra in cadena:
    print(letra)
print("Fin del bucle con cadenas")
# for con tuplas
tupla = (1, 2, 3)
for numero in tupla:
    print(numero)
print("Fin del bucle con tuplas")
# for con conjuntos
conjunto = {1, 2, 3}
for numero in conjunto:
    print(numero)
print("Fin del bucle con conjuntos")
# for con enumerar
for indice, valor in enumerate(lenguajes):
    print(f"{indice}: {valor}")
print("Fin del bucle con enumerar")
# for con zip
nombres = ["Ana", "Luis", "Carlos"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
print("Fin del bucle con zip")
# for con comprensiones de listas
cuadrados = [x**2 for x in range(5)]
print(cuadrados)
print("Fin del bucle con comprensiones de listas")
# for con comprensiones de diccionarios
edades_dict = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(edades_dict)
print("Fin del bucle con comprensiones de diccionarios")
# for con comprensiones de conjuntos
cuadrados_set = {x**2 for x in range(5)}
print(cuadrados_set)
print("Fin del bucle con comprensiones de conjuntos")
# for con funciones
def saludar(nombre):
    print(f"Hola, {nombre}!")
for nombre in nombres:
    saludar(nombre)
print("Fin del bucle con funciones")
# for con archivos
# with open("archivo.txt", "r") as archivo:
#     for linea in archivo:
#         print(linea.strip())
# print("Fin del bucle con archivos")
# for con excepciones
numeros = [1, 2, 0, 4]
for numero in numeros:
    try:
        resultado = 10 / numero
        print(f"10 dividido por {numero} es {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
print("Fin del bucle con excepciones")
# for con iteradores
iterador = iter(lenguajes)
for lenguaje in iterador:
    print(lenguaje)
print("Fin del bucle con iteradores")
# for con generadores
def generador():
    for i in range(5):
        yield i