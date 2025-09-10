lenguajes = ["Python", "JavaScript", "Java", "C++", "Ruby"]
print(lenguajes)
print(lenguajes[0]) # Python
print(lenguajes[1]) # JavaScript
print(lenguajes[-1]) # Ruby
print(lenguajes[-2]) # C++ # cuenta desde el final
print(lenguajes[1:4]) # ['JavaScript', 'Java', 'C++'] # desde el indice 1 hasta el 4 (sin incluir el 4)
print(lenguajes[2:]) # ['Java', 'C++', 'Ruby'] # desde el indice 2 hasta el final
print(lenguajes[:3]) # ['Python', 'JavaScript', 'Java'] # desde el inicio hasta el indice 3 (sin incluir el 3)
print(lenguajes[:]) # ['Python', 'JavaScript', 'Java', 'C++', 'Ruby'] # toda la lista
# modificar un elemento
lenguajes[0] = "Go"
print(lenguajes) # ['Go', 'JavaScript', 'Java', 'C++', 'Ruby']
# agregar un elemento al final
lenguajes.append("Swift")
print(lenguajes) # ['Go', 'JavaScript', 'Java', 'C++', 'Ruby', 'Swift']
# insertar un elemento en una posicion especifica
lenguajes.insert(1, "TypeScript")
