"""
Марченко Андрій 141гр.
6. Дано рядок. Якщо в цьому рядку буква f зустрічається тільки один раз, виведіть її індекс. Якщо
вона зустрічається два і більше разів, виведіть індекси її першої і останньої появи. Якщо буква f в
цьому рядку не зустрічається, нічого не виводьте.
"""

import re


def f_founder(text: str):
    text = text.lower()
    first_index = text.find("f")
    last_index = text.rfind("f")
    if first_index == last_index and first_index != -1:
        return first_index
    elif first_index != last_index:
        return "First index is " + str(first_index) + " and last index is " + str(last_index)
    else:
        return None


String = input("Enter a text: ")
print(f_founder(String))
