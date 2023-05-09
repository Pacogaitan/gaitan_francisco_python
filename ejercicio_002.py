sex = str(input("¿Que genero eres (M/F)? "))
name = str(input("Escribe tu nombre: "))
name = name.upper()
sex = sex.upper()

if name >= "N" and sex == "M":
    print("Grupo A")
elif name < "M" and sex == "M":
    print("Grupo B")
elif name >= "N" and sex == "F":
    print("Grupo B")
else: 
    print("Grupo A")