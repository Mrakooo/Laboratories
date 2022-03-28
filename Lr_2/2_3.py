"""
Марченко Андрій 141
1. Дано ціле число. Якщо воно є додатним, то відняти від нього 8; в іншому разі не змінювати його.
Вивести отримане число.
"""

def positive(num):
    if(num>=0):
        num-=8
    print(num)

n=int(input("Enter a number: "))
positive(n)
input()