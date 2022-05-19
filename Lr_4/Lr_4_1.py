"""
Марченко Андрій 141гр.
1. Дано рядок. Вивести окремі слова, що входять до нього, розділені пробілами, впорядкованими за
алфавітом, в стовпчик.

"""

import re


def sort_list(text_str : str):
    str_list = text_str.split()
    str_result = ""
    for i in sorted(str_list):
        str_result = str_result + "\n " + i
    return str_result

text = input("Enter a text: ")
print(sort_list(text))
