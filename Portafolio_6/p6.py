#ejercicio de condiciones
#ejercicio 1
age = int(input("¿Cuál es tu edad? "))
if age < 18:
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

#ejercicio 2
key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

#ejercico 3
n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)

#ejercicio 4
n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")

#ejercicio 5
age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if age > 16 and income >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")

#ejercicio 6
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

#ejercicio 7
edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")
