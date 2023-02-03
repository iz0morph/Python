text = input("Введите текст, использую пробелы: ")
lst = text.split(" ")
new_lst = []
i = 1

for el in lst:
    if len(el) > 10:
        new_lst.append(el[:10])
    else:
        new_lst.append(el)

for el in new_lst:
    print(f"{i}. {el}")
    i += 1
