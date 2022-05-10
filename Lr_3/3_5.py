"""
Андрій Марченко 141гр
16. Дано додатні числа A і B (A> B). На відрізку довжиною A розміщено максимально можлива
кількість відрізків довжиною B (без накладання). Не використовуючи операції множення і ділення,
знайти довжину незайнятої частини відрізка A.
"""


def Segments(A, B):
    while A >= B:
        A -= B
    return A


while True:
    print("Segment A > Segment B")
    segment_A = int(input("Enter length of segment A: "))
    segment_B = int(input("Enter length of segment B: "))
    if segment_A > segment_B:
        break
print(Segments(segment_A, segment_B))