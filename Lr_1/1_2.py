"""
Марченко Андрій 141
16. Визначити число, яке отримано записом у зворотному порядку цифр заданого тризначного
числа.
"""
def reverse(num):
    a = num // 100
    b = num % 100 // 10 * 10
    c = num % 10 * 100
    num = a + b + c
    print(num)


num=int(input("Enter a three-digit number:"))
reverse(num)
