"""
Марченко Андрій 141гр.
Розділ 1
10. Описати функцію Swap (X, Y), яка міняє вміст змінних X і Y (X і Y - дійсні параметри,
які є одночасно вхідними та вихідними). З її допомогою для даних змінних A, B, C, D
послідовно поміняти вміст наступних пар: A і B, C і D, B і C і вивести нові значення A,
B, C, D.
"""


def Swap(X: float, Y: float):
    X, Y = Y, X
    return X, Y


def Swap_4_values(list):
    A, B, C, D = tuple(list)
    A, B = Swap(A, B)
    C, D = Swap(C, D)
    B, C = Swap(B, C)
    return A, B, C, D


i = 1
List = []
while i <=4:
    n = input("Enter a number: ")
    try:
        n = float(n)
        List.append(n)
    except ValueError:
        print("Wrong value")
        continue
    i += 1
    n = None
print("List: ", List)
print("Swap list: ", Swap_4_values(List))