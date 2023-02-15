a = int(input('Введите число: '))


def count(a):
    count_even = 0
    count_odd = 0
    if a <= 0:
        return count_even, count_odd
    count_odd += count(a // 10)[1]
    count_even += count(a // 10)[0]
    numeral = a % 10
    if numeral % 2 == 0:
        count_even += 1
        count(a // 10)
    else:
        count_odd += 1
        count(a // 10)
    return count_even, count_odd


count_even = count(a)[0]
count_odd = count(a)[1]
print(
    f'Количество четных и нечетных цифр в числе {a} соответственно равно '
    f'{count_even} и {count_odd}')
