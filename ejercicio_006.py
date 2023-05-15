pi = 3.14159265359
def area(x):
    return (pi * x **2)
x = (int(input("Cual es el radio del circulo? ")))
print(area(x))
h = int(input("¿Cual es la altura del cilindro? "))
print(area(x*h))
