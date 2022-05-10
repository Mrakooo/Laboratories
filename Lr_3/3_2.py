"""
Андрій Марченко 141гр.
6. Логічній змінній t присвоїти значення true або false залежно від того, є натуральне число k
ступенем 3 чи ні.
"""

import math

def CheckPower(power_num):
    num = 0
    i = 1
    t = 0
    while num < power_num:
        num = math.pow(3, i)
        i += 1
        if num == power_num:
            t = 1
    if t == 1:
        return True
    return False

num = int(input("Enter a number: "))
print(CheckPower(num))