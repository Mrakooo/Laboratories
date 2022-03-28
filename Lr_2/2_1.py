"""
Марченко Андрій 141
11. Дано три змінні: X, Y, Z. Якщо їх значення впорядковані за спаданням, то подвоїти їх; в іншому
випадку замінити значення кожної змінної на протилежне.
"""

def three(x,y,z):
    if(x>y and y>z):
        x*=2
        y*=2
        z*=2
    else:
        x*=-1
        y*=-1
        z*=-1
    print("x="+str(x)+" y="+str(y)+" z="+str(z))

a=float(input("Enter first value: "))
b=float(input("Enter second value: "))
c=float(input("Enter third value: "))

three(a,b,c)

input()