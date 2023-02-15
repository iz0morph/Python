def numbers():
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
    except ValueError:
        print('Введен символ вместо числа!')
        a,b=numbers()
    else:
        return a, b
    return a,b


def operation():
    op = input('Введите знак операции: ')
    ops_lst = ['+', '-', '/', '*', '0']
    try:
        ops_lst.index(op)
    except ValueError:
        print('Неверное значение')
        op=operation()
    else:
        return op
    return op


def arithmetic():
    a, b = numbers()
    op = operation()
    if op == '0':
        return print('Программа завершила свою работу.')
    elif op == '/':
        try:
            a / b
        except ZeroDivisionError:
            print('Деление на нуль невозможно.')
            arithmetic()
        else:
            res = a / b
    elif op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    print(f'{a} {op} {b} = {res}')
    return arithmetic()


arithmetic()
