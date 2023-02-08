first_distance = int(input("Введите пробег спортсмена в первый день: "))
req_distance = int(input("Введите искомое значение пробега спортсмена: "))
distance = first_distance
day = 1
while distance < req_distance:
    distance = round(distance * 1.1, 2)
    day += 1
print(f"В {day}-й день спортсмен достиг результата "
      f"- не менее {req_distance} км ")
