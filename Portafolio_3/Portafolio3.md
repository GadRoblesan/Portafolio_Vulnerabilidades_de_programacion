# Portafolio de evidencias.

## Portafolio 3.

### Day 3 portafolio de Alan

#### Video 1: Bucles indefinidos 

bucles son ideales para las tareas que de repiten 1 y otra vez, cuando uses while debes recordar que la condicion debe regresar un True or Fals, el bucle seguira trabajando hasta que regrese un fals

EJERCICIO 1: CREAR UN WHILE SOBRE TACOS 

- #video 1 bucles (while)
- #Ejercicio 1 bucle de tacos
- nivel_hambre=4
- #damos un valor inicial
- #a una variable
- #come 4 tacos para estar satisfecho 
- while nivel_hambre>0:
-    print(f"Quieres comer {nivel_hambre} tacos")
-    print("te comes un tacos")
-    nivel_hambre=nivel_hambre-1
- print("satisfechos")

es muy importante tener una variable de interacion si no tendremos un bucle infinito sin limite y saldria error "nivel_hambre=nivel_hambre-1" para poder ir desminullendo el limite mayor a 0

#### video 2: Input()

imput: le permite al usuario que escriba un valor y lo convierte en un string y lo regresa como texto

Ejermplo 1:

- #video 2 INPUT
- print("Escribe tu nombre")
- nombre= input()
- print(f"Hola {nombre}")

dentro de input() es posible agregar algunt texto, pregunta, etc..

EJERCICIO 1: 
- #ejercicio 1 amor 
- def amor():
-    cantidad_amor=input("¿cuanto me amas?: ")
-    print(f"te amo {cantidad_amor*2}")
- amor ()

a simple vista vemos que a la hora de que demos una respuesta en el input no nos va a multiplicar 1 resultado si no que va a repetir el texto es por eso que utilizaremos TRY Y EXCEPT, el try lo usamos para ponerlo en la linea del codigo que creemos que puede causar problemas, except pondremos el mensaje que arrojara error para evitar que python explote 

- #ejercicio 1 amor
- def amor():
-    cantidad_amor=input("¿cuanto me amas?: ")
-    try:
-    cantidad_amor=int(cantidad_amor)
-    print(f"te amo {cantidad_amor*2}")
-    except:
-    print("eso no es un numero")
- amor ()

#### video 3: uso de break y continue

break: lo usamos para detener el bucle infinito dandole un alto caundo ingresemos un dato determinado 

continue: lo usamos para que en el bucle en una cierta linea se detenga y que nos mande de regreso al inicio del bucle cuando se cumpla la condicion que nosotros cumplamos 

ejemplo de break: 
- #video 3 break y continue
- #ejemplo de break
- while True:
-    internet=input("¿ de que esta hecho el internet?: ")
-    if internet=="memes"
-       break
-print("> lo sabes todo")

ejemplo de continue:
- # ejemplo de continue
- while True:
-    internet=input("¿ de que esta hecho el internet?: ")
- if internet=="":
-    print("> ¿nada? :(")
-    continue
- if internet=="memes"
-       break
-print("> lo sabes todo")

como conclusion la diferencia de break y continue es que break te saca del bucle y lo termine y continue te regresa al inicio del bucle

#### video 4: bucles definidos (for)

este tipo de bucles son definidos lo que significa que se repetira en una secuencia de valores 
 
ejemplo 1:
- #video 4 bucle definido for 
- amigos=["jojo","shrek","zerotwo"]
- for nombre in amigos:
-   print ("Hola", nombre)

ejercicio 1: bucle definido del promedio de gases al dia 
- #ejercicio 1 gases
- pedos=[1,2,3,1,2,3,100]
- total=0
- n=0
- for valor in gases:
-    total+=valor
-    #tambien puede representarse total=total+valor
-    n+=1
- print("pedos promedio por semana:", str(total/n))

con esto termino mi 3 portafolio del dia 30/10/2022
