# Portafolio de evidencias.

## Portafolio 2.

Dia 2 de programacion en python 

##Video 1: iniciamos conociendo el if,elif,else ¿Condicionales en python?

Utilizaremos operadores de comparacion:

- a == b: es igual que b 
- a != b: a es diferente que b 
- a < b: a es menor o igual que b 
- a > b: a es mayor que b 
- a >= b: a es mayor o igual que b 

ejemplo:
- nota = 8
- ¿Es la nota mayor a 6?
- #### ¿nota>6?
- if true ---> "aprobado"
- else false --->"no aprobado"

#### CODIGO:

- nota=8
- #la escala es del 0 al 10
- def notafinal(nota):
-      if nota>6:
-       return "apronado"
-    else:
-        return "no aprobado"
-print(notafinal(nota))

ELIF:

¿es la nota mayor a 8?

#### ¿nota>8?

if true---> "mencion honorifica"

elif false ---> ¿es la nota>6?

true ---> "aprobado"

false---> ¿es la nota==0?

true--> return "NP(NO PRESENTO EXAMEN)

false---> else "no aprobado"

CODIGO:

nota=8

#la escala es de 0 a 10

def notafinal(nota):

    if nota>=8
    
    return "mencion honorifica"
    
elif nota>6:

    return "aprobado"
    
elif nota==0:

    return "NP"
    
else:

    return "no aprobado"

print(notafinal(nota))

### video 2 AND, OR, NOT (OPERADORE LOGICOS)

- AND: Se usa cuando queremos que se use 1 o mas condiciones a la vez (o al mismo tiempo)

CODIGO: 

#video 2 

pepperoni= True 

albahaca= True 

if (pepperoni== True and albahaca==True):

    print("pizza de pepperoni y albahaca")
    
else:

    print("solo hay un ingrediente disponible")

- OR: Es util cuando necesitamos que se cumpla 1 funsion nada mas 

CODIGO: 
#OPERADOR OR

pepperoni=False 

albahaca=True 

if (pepperoni==True or albahaca==True):

    print("Estamos preparando su orden..")
    
else:

    print("elije un ingredeinte")
    
NOT: 
-NOT: voltea el resultado 

CODIGO: 
#operador logico # NOT

albahaca= False

if not albahaca==True:

    print("Pizza de pepperoni")
    
else:

    print("Oizza Vegetariana")
    
#ejemplo 2

ingredientes=["pepperoni","albahaca"]

if "camaron" not in ingredientes:

    print("camaron no esta disponible")
    
### comentarios: deje hasta aqui los videos porque todavia sigo paracticando estos operadores logicos

### videos del canal de SnekCato 
