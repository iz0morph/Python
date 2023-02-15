a = int(input('Введите число: '))


def reverse(a):
    if a<=0:
        return ''
    rev_a = str(a % 10) + str(reverse(a // 10))
    return rev_a


print(f'Число {a}, записанное в обратном порядке: {reverse(a)}')
