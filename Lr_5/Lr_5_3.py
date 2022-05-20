"""
Марченко Андрій 141гр.
Розділ 3
10. Описати функцію IsDistance(X, Y) дійсного типу, яка обчислює відстань між двома
точками, заданими своїми координатами. За допомогою цієї функції знайти
периметр десятикутника, вершини якого мають відповідно координати (x1, y1), (x2,
y2), …, (x10, y10).
"""


from math import sqrt


def IsDistance(X, Y):
    x1, y1 = X
    x2, y2 = Y
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def PerimeterOfDecagon(list):
    x = 0
    y = 1
    perimeter = 0
    list2 = []
    for i in list:
        list2.append(IsDistance(list[x], list[y]))
        perimeter += IsDistance(list[x], list[y])
        x += 1
        if y == 9:
            y = 0
        else:
            y += 1
    print("The list of distances:\n", list2)
    return perimeter


i = 1
List = []
while i <= 10:
    x = input("Enter X: ")
    y = input("Enter Y: ")
    try:
        x = float(x)
        y = float(y)
        z = x, y
        List.append(z)
    except ValueError:
        print("Wrong value")
        continue
    i += 1
    x = None
print("List: ", List)
print("Perimeter: ", PerimeterOfDecagon(List))