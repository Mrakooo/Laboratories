"""
Марченко Андрій 141
12. Дано чотири цілих числа, одне з яких відмінно від трьох інших, рівних між собою. Вивести
порядковий номер цього числа.
"""

def imposter(n1,n2,n3,n4):
    if(n1==n2 and n2==n3):
        print("The 4th is an imposter")
    elif (n1 == n2 and n2 == n4):
        print("The 3d is an imposter")
    elif (n3 == n2 and n2 == n4):
        print("The 1st is an imposter")
    elif (n1 == n3 and n3 == n4):
        print("The 2d is an imposter")

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2d number: "))
num3=int(input("Enter 3d number: "))
num4=int(input("Enter 4th number: "))
imposter(num1, num2, num3, num4)
