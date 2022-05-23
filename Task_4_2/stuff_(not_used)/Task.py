"""
Марченко Андрій 141гр.    Варіант 4|2
Завдання:
1. Запитати у користувача код регіону
2. Отримати ЗВО з вказаного користувачем регіону
3. Зберегти всі дані у файл universities.csv у форматі csv
4. Збережіть ті ж дані у файл universities_<код регіону>.csv, наприклад universities_80.csv
5. Якщо регіон не зі списку доступних, то повідомити про це користувачеві у консолі
Завдання #1
4. Назви та EDRPOU в файл EDRPOU.csv
Завдання #2
2. З посадою керівника Ректор
Завдання 3
Ускладніть програму з другого завдання можливістю фільтрування за будь-яким з наявних значень поля
Підказка - сформуйте список всіх значень що зустрічають і дайте користувачеві обрати
"""


import csv
import requests



# def function_continue(key_y_or_n):
#     while True:
#         continue_key = input("Do you want to enter another key? (Y/N): ")
#         if continue_key in "Nn":
#             return False
#         elif continue_key in "Yy":
#             return True
#         else:
#             print("Enter Y or N")
#             continue


def function_user_choice():
    print("\nThere are some items that can be added:\n",
          "З формою фінансування Державнa (key 1)\n",
          "З посадою керівника Ректор (key 2)\n",
          "З роком заснування між 1950 та 1999 (key 3)\n")
    print("What information should be added? Enter key(s) to add information or 'skip' to skip this step")
    list_of_keys = []
    key_of_info = ""
    while True:
        key = input("Enter key(s): ")
        if "skip" in key:
            break
        if "1" in key:
            key_of_info += "1"
            list_of_keys.append(1)
        if "2" in key:
            key_of_info += "2"
            list_of_keys.append(2)
        if "3" in key:
            key_of_info += "3"
            list_of_keys.append(3)
        list_of_keys.sort()
        if list_of_keys == []:
            print("The key(s) does not match allowed value, enter allowed key(s), please:")
            continue
        break
    return key_of_info


def check(region, list_of_regions_codes):
    a = region in list_of_regions_codes
    if a is False:
        print('Enter another code')
        return get_region()
    else:
        return region


def show_list_of_codes_and_regions(index=0, key=False, key2=False):
    list_of_codes_and_regions = ["01 | Автономна Республіка Крим",
                                 "05 | Вінницька область",
                                 "07 | Волинська область",
                                 "12 | Дніпропетровська область",
                                 "14 | Донецька область",
                                 "18 | Житомирська область",
                                 "21 | Закарпатська область",
                                 "23 | Запорізька область",
                                 "26 | Івано-Франківська область",
                                 "32 | Київська область",
                                 "35 | Кіровоградська область",
                                 "44 | Луганська область",
                                 "46 | Львівська область",
                                 "48 | Миколаївська область",
                                 "51 | Одеська область",
                                 "53 | Полтавська область",
                                 "56 | Рівненська область",
                                 "59 | Сумська область",
                                 "61 | Тернопільська область",
                                 "63 | Харківська область",
                                 "65 | Херсонська область",
                                 "68 | Хмельницька область",
                                 "71 | Черкаська область",
                                 "73 | Чернівецька область",
                                 "74 | Чернігівська область",
                                 "80 | Київ",
                                 "85 | м.Севастополь"]

    list_of_codes_of_regions = ["01", "05", "07", "12", "14",
                                "18", "21", "23", "26", "32",
                                "35", "44", "46", "48", "51",
                                "53", "56", "59", "61", "63",
                                "65", "68", "71", "73", "74",
                                "80", "85"]

    if key2 == True:
        return list_of_codes_of_regions
    if key == True:
        return list_of_codes_and_regions[index]
    return list_of_codes_and_regions


def get_region():
    print("There is a list of codes of regions:")
    index = 0
    for i in show_list_of_codes_and_regions():
        print(show_list_of_codes_and_regions(index, key=True))
        index += 1
    region = str(input("Enter the region code: "))
    return check(region, show_list_of_codes_and_regions(key2=True))


def get_zvo_list(region):
    zvo = requests.get(
        'https://registry.edbo.gov.ua/api/universities/?ut=1&lc='+region+'&exp=json')
    try:
        list_of_universities: list = zvo.json()
    except Exception as ex:
        return print("Could not access the list of universities {}".format(region)), exit(0)
    return list_of_universities


# def check_info(list_of_edrpou_info, key_of_info=""):
#     index = 0
#     for i in list_of_edrpou_info:
#         if "1" in key_of_info and "3" in key_of_info:
#             if "No" in i:
#                 list_of_edrpou_info.pop(index)
#         if "1" in key_of_info:
#             if "No" in i[3]:
#                 list_of_edrpou_info.pop(index)
#         if "3" in key_of_info:
#             if "No" in i[4]:
#                 list_of_edrpou_info.pop(index)
#         if "No" in i[2]:
#             i.pop(2)
#         if "No" in i[3]:
#             i.pop(3)
#         index += 1
#     return list_of_edrpou_info


def find_edrpou_info(zvo_list, key_of_info=""):
    index = 0
    list_whole_info = []
    list_edrpou_info = []
    list_rector_info = []
    new_dict = {}
    university_financing_type_name = ""
    registration_year = ""
    for i in zvo_list:
        new_dict.update(zvo_list[index])
        university_name = new_dict['university_name']
        university_edrpou = new_dict['university_edrpou']
        if "1" in key_of_info:
            university_financing_type_name = new_dict['university_financing_type_name']
            if university_financing_type_name != 'Державна':
                university_financing_type_name = ""
        university_director_fio = new_dict['university_director_fio']
        if "3" in key_of_info:
            registration_year = new_dict['registration_year']
            try:
                if not (int(registration_year) >=1950 and int(registration_year) <= 1999):
                    registration_year = ""
            except TypeError:
                registration_year = ""
        new_dict.clear()
        new_list_whole_info = [university_name, university_edrpou, university_director_fio, university_financing_type_name, registration_year]
        new_list_edrpou_info = [university_name, university_edrpou]
        new_list_rector_info = [university_name, university_director_fio]
        list_whole_info.append(new_list_whole_info)
        list_edrpou_info.append(new_list_edrpou_info)
        list_rector_info.append(new_list_rector_info)
        index += 1
    return list_whole_info, list_edrpou_info, list_rector_info
#    return check_info(list_whole_info, key_of_info), list_edrpou_info, list_rector_info


def write_in_csv(whole_info, edrpou_info, rector_info, region, user_choise):
    with open('universities_' + region + '.csv', mode='w', encoding='CP1251') as f:
        f.write(str(whole_info))
    with open('edrpou.csv', mode='w', encoding='CP1251') as g:
        g.write(str(edrpou_info))
    if "2" in user_choise:
        with open('edrpou.csv', mode='w', encoding='CP1251') as h:
            h.write(str(rector_info))


def main():
    region = get_region()
    zvo_list = get_zvo_list(region)
    user_choice = function_user_choice()
    whole_info, edrpou_info, rector_info,  = find_edrpou_info(zvo_list, user_choice)
    write_in_csv(whole_info, edrpou_info, rector_info, region, user_choice)
    # print(zvo_list)
    # print(whole_info)
    # print(edrpou_info)
    # print(rector_info)
main()
