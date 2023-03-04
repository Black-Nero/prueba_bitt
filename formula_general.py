# formula general

a=float(input("Introduzca el valor de a: "))
b=float(input("Introduzca el valor de b: "))
c=float(input("Introduzca el valor de c: "))

x1= ((-b+((b*b)-(4*a*c))**0.5)/(2*a))
x2= ((-b-((b*b)-(4*a*c))**0.5)/(2*a))

print("el valor de de x1 es: ")
print(x1)

print("El valor de x2 es: ")
print(x2)