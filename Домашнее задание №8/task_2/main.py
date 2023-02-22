import json


def get_json_obj():
    with open("orders.json") as file:
        obj = json.load(file)
    return obj


def write_order_to_json():
    obj = get_json_obj()
    lst = obj['orders']
    with open("orders.json", 'w', encoding='utf-8') as file:
        while input('Добавить позицию?\n') == 'да':
            item = input('Введите название товара: ')
            quantity = input('Введите количество товара в заказе: ')
            price = input('Введите цену товара: ')
            buyer = input('Введите ФИО покупателя: ')
            date = input('Введите дату заказа: ')
            new_order = {'item': item, 'quantity': quantity, 'price': price,
                         'buyer': buyer, 'date': date}
            lst.append(new_order)
            if input('Очистить список заказов?\n') == 'да':
                lst.clear()
            else:
                pass
        json.dump(obj, file, indent=4)


write_order_to_json()
