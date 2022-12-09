# Portafolio de evidencias.

## Portafolio 8.

#ejercicios de utilizacion de FOR
#ejercicio 1 multiplicaciones
numero = int(input("Numero a multiplicar: "))

print("Tabla de multiplicar:")
for n in range (1, 11):
    #if n % 2 == 0:
        print("{} x {} = {}".format(numero, n, n * numero))

print("Tabla de divicion:")
for n in range (1, 11):
    print("{} / {} = {}".format(numero, n, n % numero))


#ejercicio 2 organizar textos solicitados
punto = 0
coma = 0
espacio= 0
texto = input("Introduzca su texto:")
for a in texto:
    if a == ".":
        punto += 1
    elif a == ",":
        coma += 1
    else:
        espacio += 1

print("Su texto posee "+ str(punto) + " puntos")
print("Su texto posee "+ str(coma) + " comas")
print("Su texto posee "+ str(espacio) + " espacios")

con estos ejercicios logras tener un rango mayor en saber utilizar python, el poder hacer operaciones es algo sencillo pero muy util en todo sistema operativo y el saber usar el for que es algo que se usa simpre en cualquier programacion es muy importante y necesario asi que con esto queda saldado el conocer estos conceptos basicos 
