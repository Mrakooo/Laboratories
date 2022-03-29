"""
Марченко Андрій 141
6. Поміняти місцями вміст змінних A і B і вивести нові значення A і B.
"""

def reverse_a_b():
    A = "True"
    B = 141
    C = None
    print("A=" + str(A))
    print("B=" + str(B))

    print("----------")

    C = A
    A = B
    B = C
    print("A=" + str(A))
    print("B=" + str(B))


reverse_a_b()
