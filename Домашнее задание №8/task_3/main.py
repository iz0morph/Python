"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml


def data_to_yaml():
    qt_items = int(input("Введите кол-во позиций: "))
    items_list = []
    for i in range(qt_items):
        i = input("Введите название товара: ")
        items_list.append(i)
    items_dict = {}
    for i in items_list:
        price = input(f'Введите цену товара ({i}): ')
        new_price = {f'{i}': f'{price} €'}
        items_dict.update(new_price)
    data_dict = {'items': items_list, 'items prices': items_dict,
                 'items quantity': qt_items, }
    return data_dict


def read_yaml():
    with open('file.yaml') as file:
        file_data = yaml.load(file, Loader=yaml.FullLoader)
    return file_data


def write_to_yaml():
    data_dict = data_to_yaml()
    file_data = read_yaml()
    if file_data != data_dict:
        with open('file.yaml', 'w', encoding='utf-8') as file:
            yaml.dump(data_dict, file, default_flow_style=False,
                      allow_unicode=True)
    else:
        print('Введенные данные уже есть в файле: ')


write_to_yaml()
