class not_number(Exception):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'quit':
            break
        if not value.isdigit():
            raise not_number(value)
        my_list.append(int(value))
    except not_number as el:
        print('Не число!', el)
    else:
        print(my_list)
print(my_list)