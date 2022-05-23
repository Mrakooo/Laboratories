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


def show_list_of_codes_and_regions(index=0, key=False, key2=False): # Надає список та код регіонів
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


def check(region, list_of_regions_codes): # Перевіряє наявність коду регіону у списку регіонів
    a = region in list_of_regions_codes
    if a is False:
        print('Enter another code')
        return get_region()
    else:
        return region


def get_region(): # Запитує який регіон треба обрати
    print("There is a list of codes of regions:")
    index = 0
    for i in show_list_of_codes_and_regions():
        print(show_list_of_codes_and_regions(index, key=True))
        index += 1
    region = str(input("Enter the region code: "))
    return check(region, show_list_of_codes_and_regions(key2=True))


def function_user_choice(): # Пропонує користувачеві надати додаткову інформацію
    print("\nThere are some items that can be added:\n",
          "З формою фінансування (key 1)\n",
          "З посадою керівника Ректор (key 2)\n",
          "З роком заснування між 1950 та 1999 (key 3)\n")
    print("What information should be added? Enter key(s) to add information or 'skip' to skip this step")
    list_of_keys = []
    key_of_info = ""
    while True: # Перевіряє наданий ключ
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
    return key_of_info # Повертає ключі, за допомогою яких буде надана додаткова інформація


def write_in_csv(region, key_of_info): # Записує усю надану інформацію у файли

    r = requests.get('https://registry.edbo.gov.ua/api/universities/?ut=1&lc=' + region + '&exp=json')
    try:
        universities: list = r.json()
    except Exception as ex:
        return print("Could not access the list of universities {}".format(region)), exit(0)

    # Основний файл
    filtered_data = [{k: row[k] for k in ['university_name',
                                          'university_parent_id',
                                          'university_edrpou',
                                          'university_director_fio',
                                          'university_email',
                                          'university_phone',
                                          'post_index',
                                          'university_address',
                                          'university_financing_type_name',
                                          'registration_year'
                                          ]} for row in universities]

    with open('universities_' + region + '.csv', mode='w', encoding='CP1251') as f:
        writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
        writer.writeheader()
        writer.writerows(filtered_data)

    # Записує тип фінансування обрану користувачем
    if "1" in key_of_info:
        while True:
            financing_type = input("Enter financing type (Державна|Приватна|Комунальна): ")
            if financing_type not in ["Державна", "Приватна", "Комунальна"]:
                print("There is no allowed value, enter allowed value, please")
                continue
            else:
                break

        filtered_data = [{k: row[k] for k in ['university_name',
                                              'university_financing_type_name']} for k in ['university_financing_type_name']
                         for row in universities
                         if row[k] == financing_type]

        with open('financing_type_' + region + '.csv', mode='w', encoding='CP1251') as f:
            writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
            writer.writeheader()
            writer.writerows(filtered_data)

    # Записує ПІБ ректорів
    if "2" in key_of_info:
        filtered_data = [{k: row[k] for k in ['university_name',
                                              'university_director_fio',]} for row in universities]

        with open('rector_fio_' + region + '.csv', mode='w', encoding='CP1251') as f:
            writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
            writer.writeheader()
            writer.writerows(filtered_data)

    # Записує контактну інформацію ВУЗів, які були зареєстровані з 1950 по 1999 років
    if "3" in key_of_info:
        filtered_data = [{k: row[k] for k in ['university_name', 'university_address', 'university_email', 'post_index', 'registration_year']} for row in
                         list(filter(lambda x: 1999 > int(x['registration_year'] or 0) > 1950, universities))]

        with open('from_1950_to_1999_' + region + '.csv', mode='w', encoding='CP1251') as f:
            writer = csv.DictWriter(f, fieldnames=filtered_data[0].keys())
            writer.writeheader()
            writer.writerows(filtered_data)


def main():
    write_in_csv(get_region(), function_user_choice())


main() # Запускає програму
