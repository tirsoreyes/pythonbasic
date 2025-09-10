edad = 22
print(edad > 18 and edad < 30) # True
print(edad > 18 or edad < 30) # True
print(not(edad > 18)) # False
print(edad > 18 and not(edad < 30)) # False
print(edad > 18 or not(edad < 30)) # True
print(edad > 18 and edad < 30 and edad == 22) # True
print(edad > 18 and edad < 30 and edad == 23) # False
print(edad > 18 or edad < 30 or edad == 23) # True
print(edad > 18 or edad < 30 or edad == 22) # True
print(edad > 18 or edad < 30 or edad == 23) # True
print(edad > 18 and (edad < 30 or edad == 23)) # True
print((edad > 18 and edad < 30) or edad == 23) # True
print((edad > 18 and edad < 30) or edad == 22) # True
print((edad > 18 and edad < 30) or edad == 23) # True
