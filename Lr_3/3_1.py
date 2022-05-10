"""
Андрій Марченко 141гр.
1. Підрахувати k - кількість цифр в десятковому запису цілого невід'ємного числа n.
"""

def value():
    num = int(input("Enter an integer number: "))
    return len(str(num))

print('Amount of numbers in', value())