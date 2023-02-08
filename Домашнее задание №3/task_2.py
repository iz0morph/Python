new_value = int(input("Введите целое положительное число: "))
rating = [56, 48, 22, 22, 10, 10, 1]
i = -1
while abs(i) <= len(rating):
    if new_value <= rating[i]:
        rating.insert(i + 1, new_value)
        break
    if abs(i) == len(rating):
        rating.insert(0, new_value)
        break
    i += -1
print(rating)
