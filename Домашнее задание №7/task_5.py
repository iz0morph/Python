class NotNumber(Exception):
    pass


my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'quit':
            break
        if not value.isdigit():
            raise NotNumber(value)
        my_list.append(int(value))
    except NotNumber as el:
        print('Не число!', el)
    else:
        print(my_list)
print(my_list)
