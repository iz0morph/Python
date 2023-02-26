class Validation:
    def __set__(self, instance, value):
        if type(value) is not str:
            raise TypeError(f'{self.my_attr} не является строкой!')
        elif value == '':
            raise ValueError(f'{self.my_attr} - пустая строка!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = Validation()
    surname = Validation()
    position = Validation()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return (f"{self.name} {self.surname}")

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


new_worker = Position('Иван', 'Иванов', 'искусствовед', 50, 15)
print(f'Сотрудник: {new_worker.get_full_name()}, '
      f'{new_worker.position}, оклад: {new_worker._income["wage"]}, премия: '
      f'{new_worker._income["bonus"]}')
print(f'Итоговая зарплата {new_worker.get_full_name()} - '
      f'{new_worker.get_full_salary()}')
