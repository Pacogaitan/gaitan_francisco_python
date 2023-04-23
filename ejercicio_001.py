'''
Name = "Francisco"
FirstLastName = "Gaitan"
SecondLastName = "Bandala"
BornYear = 1988
BornMonthDay = "02-08"
'''
Name = input("¿Cuál es tu nombre?")
type(Name)
FirstLastName = input("¿Cuál es tu primer apellido?")
type(FirstLastName)
SecondLastName = input("¿Cuál es tu segundo apellido?")
type(SecondLastName)
BornYear = input("¿En qué año naciste?")
type(BornYear)
#BornYear=int
BornMonthDay = input("¿En qué mes y día naciste? (MM-DD):")
type(BornMonthDay)

CurrentYear = 2023

print("Este es tu nombre completo en mayúsculas:")
FullName = Name + " " + FirstLastName + " " + SecondLastName
print (FullName.upper())
print("\nEste es tu nombre completo en minúsculas:")
print (FullName.lower())
print("\nEsta es tu fecha de nacimiento:")
print(BornMonthDay,"-",BornYear)
Lenght = len(Name)+ len(FirstLastName)+ len(SecondLastName)
Age=CurrentYear-int(BornYear)
print("\nEsta es tu edad", Age)
print("\nTu nombre completo tiene",len([char for char in FullName if char in "aeiou"]),"vocales")
print("\nTu nombre completo tiene", Lenght, "letras") 
print("\n¿Tu edad es un caracter de tipo número?", isinstance(Age, int))
print("\n¿Tu nombre completo es un carácter de tipo alfanumerico?", isinstance(FullName, str)) 
print("\nTu edad en 10 años será de",Age+10)
print("\nLa media de tu edad actual y tu edad en 20 años es de", (Age*2+20)/2)