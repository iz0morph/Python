lst = input("Введите целые числа через пробел: ").split(" ")
i = 0
while i < len(lst) - 1:
    temp = lst[i]
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    i += 2
print(lst)
