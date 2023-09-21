def suma(a,b):
  x = a + b
  return x

def resta (a,b):
  x = a - b
  return x

print("Dame el primer numero:")
a = int(input())
print("dame el segundo numero:")
b = int(input())
print("La suma da ",suma(a,b), "y la resta da",resta(a,b))


def multiplicación(a,b):
  x = a * b
  return x

def división(a,b):
  x = a/b
  return x

print("Dame el primer numero:")
a = int(input())
print("dame el segundo numero:")
b = int(input())
print("la multiplicación da ", multiplicación(a,b), "y la división da ", división(a,b))


def conversión():
  print("dime cuantos kilometros recorriste y lo transformaré a metros")
  kilometros = int(input())
  operación = kilometros*1000
  print(operación)

conversión()



def area_triangulo():
  

  print("dame la base del triangulo")
  a = int(input())
  print("dame la altura")
  b = int(input())
  area = int(a)*int(b)/2
  print("el area del triangulo es ", area)
area_triangulo()
