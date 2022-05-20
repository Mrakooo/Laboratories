"""
Марченко Андрій 141гр.
Розділ 5
5. Описати функцію RearRange(x, y), яка перевіряє, чи можливо переставивши букви в
слові х отримати слово y.
"""


def RearRange(x, y):
    x = sorted(list(x))
    y = sorted(list(y))
    if x == y:
        return True
    return False


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
if RearRange(word1, word2) == True:
    print("You can make second word from first word")
else:
    print("The letters don't coincide")
