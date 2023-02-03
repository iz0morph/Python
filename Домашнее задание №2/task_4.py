lst = input("Введите целые числа через пробел: ").split(" ")
temp = ""
i = 0
while i < len(lst) - 1:
    temp = lst[i]
    lst[i] = lst[i + 1]
    lst[i + 1] = temp
    i += 2
print(lst)
