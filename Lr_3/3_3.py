"""
Андрій Марченко 141гр.
11. Дано число A (> 1). Вивести найменше з цілих чисел K, для яких сума 1 + 1/2 + … + 1/K будет
більше A, і саму цю суму.
"""

def value(A, K = 1, sum = 0 ):
    sum += 1 / K
    if K > A and sum > A:
        return K
    K += 1
    return value(A, K, sum)

num = int(input("Enter a number: "))
print(value(num))