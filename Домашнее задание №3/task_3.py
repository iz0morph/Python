number_of_goods = int(input("Введите количество товаров в ассортименте: "))
lst = []
name_lst = []
price_lst = []
amount_lst = []
measure_lst = []
for i in range(number_of_goods):
    name = input("Введите название товара: ")
    price = input("Введите цену товара: ")
    amount = input("Введите количество товара: ")
    measure = input("Введите единицу измерения товара: ")
    temp_dict = {"название": name, "цена": price, "количество": amount,
                 "единица измерения": measure}
    lst.append((i + 1, temp_dict))
    name_lst.append(name)
    price_lst.append(price)
    amount_lst.append(amount)
    measure_lst.append(measure)

lst_of_char = [name_lst, price_lst, amount_lst, measure_lst]
keys = list(temp_dict)
final_dict = {}
for j in range(len(keys)):
    final_dict.update({keys[j]: lst_of_char[j]})
print(final_dict)
