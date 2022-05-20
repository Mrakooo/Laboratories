"""
Марченко Андрій 141гр.
Розділ 4
10. Описати функцію GCD2 (A, B) цілого типу, яка знаходить найбільший спільний
дільник (НСД, greatest common divisor) двох цілих позитивних чисел A і B,
використовуючи алгоритм Евкліда:
НСД (A, B) = НСД (B, A mod B), якщо B ≠ 0; НСД (A, 0) = A,
де «mod» позначає операцію взяття залишку від ділення. За допомогою GCD2 знайти
найбільші спільні дільники пар (A, B), (A, C), (A, D), якщо дано числа A,
B, C, D
"""


def GCD2(A, B):
    while A != 0 and B != 0:
        if A > B:
            A = A % B
        else:
            B = B % A
    return A + B


def GCD2_for4Values(list):
    list2 = []
    i = 1
    while i <= len(list) - 1:
        list2.append(GCD2(list[0], list[i]))
        i += 1
    return list2

i = 1
List = []
while i <= 4:
    x = input("Enter a number: ")
    try:
        x = int(x)
        List.append(x)
    except ValueError:
        print("Wrong value")
        continue
    i += 1
    x = None
print("List: ", List)
print("GCD: ", GCD2_for4Values(List))