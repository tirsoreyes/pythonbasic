lenguajes = ["Python", "JavaScript", "Java", "C++", "Ruby"]

print("Pythonn" in lenguajes) # False
print("Python" in lenguajes) # True
print("Java" not in lenguajes) # False
print("Swift" not in lenguajes) # True
print(len(lenguajes)) # 5
lenguajes.insert(1, "TypeScript")
print(lenguajes) # ['Go', 'TypeScript', 'JavaScript', 'Java', 'C++', 'Ruby', 'Swift']
# eliminar un elemento por su valor
lenguajes.remove("Java")
print(lenguajes) # ['Go', 'TypeScript', 'JavaScript', 'C++', 'Ruby', 'Swift']
# eliminar un elemento por su indice
del lenguajes[3]
print(lenguajes) # ['Go', 'TypeScript', 'JavaScript', 'Ruby', 'Swift']
# eliminar el ultimo elemento y retornarlo
ultimo = lenguajes.pop()
print(ultimo) # Swift
print(lenguajes) # ['Go', 'TypeScript', 'JavaScript', 'Ruby']
# obtener el indice de un elemento
indice = lenguajes.index("JavaScript")
print(indice) # 2
# contar cuantas veces aparece un elemento
count = lenguajes.count("Python")
print(count) # 0
# ordenar la lista (alfabeticamente)
lenguajes.sort()
print(lenguajes) # ['Go', 'JavaScript', 'Python', 'Ruby', 'TypeScript']
# ordenar la lista (alfabeticamente) en orden inverso
lenguajes.sort(reverse=True)
print(lenguajes) # ['TypeScript', 'Ruby', 'Python', 'JavaScript', 'Go']
# invertir el orden de la lista
lenguajes.reverse()
print(lenguajes) # ['Go', 'JavaScript', 'Python', 'Ruby', 'TypeScript']
# obtener la longitud de la lista
longitud = len(lenguajes)
print(longitud) # 5
# limpiar la lista (eliminar todos los elementos)
lenguajes.clear()
print(lenguajes) # []