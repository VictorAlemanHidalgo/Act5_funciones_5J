print("Ejemplo de funciones")
#Declarando funciones
def hola():
    print("Alguien uso la funcion hola")

def chat(mensa):
    print(f"Chat: {mensa}")

def ellaContesta(mensa):
    print(f"Chat ella: {mensa}")

def escribeNombre(ap, n):
    print(f"Tu nombre completo es: {n} {ap}")

def suma(a,b):
    s = a + b
    return s

def resta(a,b):
    s = a - b
    return s

def multiplicacion(a,b):
    s = a * b
    return s

def division(a,b):
    s = a / b
    return s

# Llamadas a funciones
hola()
chat("Que bonita estas")
ellaContesta("Gracias")
escribeNombre("Aleman", "Victor")
print("Operaciones suma")
c1 = int(input("Ingresa un numero: "))
c2 = int(input("Ingresa un numero: "))
dameSuma=suma(c1, c2)
print(f"La suma de {c1} + {c2} = {dameSuma}")

print("Operaciones resta")
c3 = int(input("Ingresa un numero: "))
c4 = int(input("Ingresa un numero: "))
dameResta=resta(c3, c4)
print(f"La resta de {c3} - {c4} = {dameResta}")

print("Operaciones multiplicacion")
c5 = int(input("Ingresa un numero: "))
c6 = int(input("Ingresa un numero: "))
dameMultiplicacion=multiplicacion(c5, c6)
print(f"La multiplicacion de {c5} * {c6} = {dameMultiplicacion}")

print("Operaciones division")
c7 = int(input("Ingresa un numero: "))
c8 = int(input("Ingresa un numero: "))
dameDivision=division(c7, c8)
print(f"La division de {c7}/{c8} = {dameDivision}")