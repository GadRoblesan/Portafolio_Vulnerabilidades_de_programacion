#ejercicio 1 de cadenas
nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))

#ejercicio 2
name = input("¿Cómo te llamas? ")
print(name.lower())
print(name.upper())
print(name.title())

#ejercicio 3
nombre = input("¿Cómo te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

#ejercicio 4
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])

#ejercicio 5
frase = input("Introduce una frase: ")
print(frase[::-1])

#ejecicio 6
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))

#ejercicio 7
email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')

#ejercicio 8
precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

#ejercicio 9
fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])

#ejercicio 10
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))

#ejercicio 11
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
