"""
Марченко Андрій 141гр.
11. Дано список. Вивести спочатку всі негативні елементи, а потім всі інші.

"""

def negative_list(List):
    negative = []
    positive = []
    for i in List:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    return negative + positive


n = []

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
    n.append(m)
    m = None


print(negative_list(n))
