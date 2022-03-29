"""
Марченко Андрій 141
6. Дано ціле число в діапазоні 1-7. Вивести рядок - назва дня тижня, що відповідає даному числу (1 -
«понеділок», 2 - «вівторок» і т. д.).
"""

def week(num):
    if(num==1):
        print("Понеділок")
    elif (num==2):
        print("Вівторок")
    elif (num==3):
        print("Середа")
    elif (num==4):
        print("Четвер")
    elif (num==5):
        print("П'ятниця")
    elif (num==6):
        print("Субота")
    elif (num==7):
        print("Неділя")

n=int(input("Enter a number from 1 to 7: "))
week(n)
