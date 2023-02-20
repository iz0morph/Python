class Worker:

    def __init__(self, name, surname,position, wage, bonus ):
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