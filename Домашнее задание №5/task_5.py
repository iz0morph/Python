a = 32
b = 127
temp = 32


def ascii_table(a, b, temp):
    if temp == 127:
        return f'{temp} - {chr(temp)}'
    if (temp - a) % 10 == 0 and temp != 32:
        el = f'{temp} - {chr(temp)} '
        return '\n' + el + ascii_table(a, b, temp + 1)
    else:
        el = f'{temp} - {chr(temp)} '
        return el + ascii_table(a, b, temp + 1)


print(ascii_table(a, b, temp))
