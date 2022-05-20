"""
Марченко Андрій 141гр.
Розділ 2
10. Описати функцію IsSquare (K) логічного типу, яка повертає True, якщо цілий
параметр K (> 0) є квадратом деякого цілого числа, і False в іншому випадку. З її
допомогою знайти кількість квадратів в наборі з 10 цілих позитивних чисел.
"""


from math import sqrt


def IsSquare(K: int):
    if sqrt(K) == int(sqrt(K)):
        return True
    return False


def IsSquareForTenNumbers(list):
    for i in list:
        print(IsSquare(i))
    return "Finish"


i = 1
List = []
while i <= 10:
    n = input("Enter a number: ")
    try:
        n = int(n)
        if n <= 0:
            continue
        List.append(n)
    except ValueError:
        print("Wrong value")
        continue
    i += 1
    n = None
print("List: ", List)
print("Is square: ", IsSquareForTenNumbers(List))