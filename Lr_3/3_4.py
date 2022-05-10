"""
Андрій Марченко 141гр.
12. Дано ціле число N (> 0), яке є деяким ступенем числа 2: N = 2^K. Знайти ціле число K — показник цієї ступені.
"""

def PowerOfTwo(N):
    K = 0
    num = 0
    while num < N:
        num = 2 ** K
        if num == N:
            return K
        K +=1
    return False
num = int(input('Enter a num that is a power of two: '))
print(PowerOfTwo(num))