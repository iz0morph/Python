number = int(input("Введите целое положительное число: "))
max_numeral = 0
temp_value = number
while temp_value > 0:
    if temp_value % 10 > max_numeral:
        max_numeral = temp_value % 10
    temp_value //= 10
print(f"Самая большая цифра в числе {number} - {max_numeral}")
