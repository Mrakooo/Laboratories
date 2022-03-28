"""
Марченко Андрій 141
11. Знайти значення функції y=3x^6+6x^2+7 при даному значенні x.

"""

def value(x):
    y = 3 * x ** 6 + 6 * x ** 2 + 7
    print(y)
    input()

x = float(input("Enter a num: "))
value(x)