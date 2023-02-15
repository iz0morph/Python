n = int(input('Введите число элементов последовательности: '))
a_0 = 1


def summ(a, n):
    if n == 0:
        return 0
    total = a + summ(a * (-0.5), n - 1)
    return total


print(f'Сумма {n} первых членов последовательности [1; -0.5; 0.25...]: '
      f'{summ(a_0, n)}')
