"""
Марченко Андрій 141гр.
18. Ввести з клавіатури числа в стовпчик до тих пір, поки не буде введено число 0. Видалити всі
непарні числа даного списку та вивести його.
"""


def even_number(List: list):
   even_list = []
   for i in List:
       if i % 2 == 0:
           even_list.append(i)
   return even_list


list = []

while True:
    m = input("Enter a number or '0' to break ")
    if m == "0":
        break
    else:
        try:
            m = int(m)
        except ValueError:
            print("Wrong value \nLet it be 2")
            m = 2
    list.append(m)
    m = None


print(even_number(list))
