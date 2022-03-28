"""
Марченко Андрій 141
16. Дано ціле число, що позначає код символу по таблиці ASCII. Визначити, це код англійської
літери або будь-якої іншої символ. (Dec)
"""

def ASCII(n):
    if(n>=65 and n<=90):
        print("This is an english letter")
    elif(n>=97 and n<=122):
        print("This is an english letter")
    else:
        print("This is any symbol")

n=int(input("Enter a number: "))
ASCII(n)
input()