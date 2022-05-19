"""
Марченко Андрій 141гр.
12. Написати програму циклічного зсуву елементів списку вліво. Наприклад, дано список:
[1,2,3,4,5,6] після зсуву на один елемент вліво, повинні отримати: [2,3,4,5,6,1].
"""


def next_left(List: list):
    print(List)
    n = [List.pop(0)]
    return List + n


list = []

while True:
    m = input("Enter a number or 'break' ")
    if m == "break":
        break
    else:
        try:
            m = int(m)
        except ValueError:
            print("Wrong value \nLet it be 0")
            m = 0
    list.append(m)
    m = None


print(next_left(list))
