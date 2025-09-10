# convertir de celcius a fahrenheit y viceversa
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32 # formula
def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9 # formula
print("Conversor de temperaturas")
opcion = input("Elige la opcion (1) Celsius a Fahrenheit (2) Fahrenheit a Celsius: ")
if opcion == "1":
    c = float(input("Ingresa la temperatura en Celsius: "))
    f = celsius_a_fahrenheit(c)
    print(f"{c} grados Celsius son {f} grados Fahrenheit")
elif opcion == "2":
    f = float(input("Ingresa la temperatura en Fahrenheit: "))
    c = fahrenheit_a_celsius(f)
    print(f"{f} grados Fahrenheit son {c} grados Celsius")
else:
    print("Opcion no valida")
# fin del programa
