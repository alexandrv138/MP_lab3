"""! Модуль с разработанным классом сотрудника бухгалтерии."""

class Employee:
    """! Класс, описывающий сотрудника"""

    def __init__(self, name, pos, dep, sal):
        """! Инициализация объекта"""
        self.name = name  # ФИО
        self.pos = pos  # Должность
        self.dep = dep  # Отдел (подразделение)
        self.sal = sal  # Зарплата

    def __lt__(self, other):
        """! Перегрузка оператора <"""
        return self.name < other.name

    def __le__(self, other):
        """! Перегрузка оператора <="""
        return self.name <= other.name

    def __gt__(self, other):
        """! Перегрузка оператора >"""
        return self.name > other.name

    def __ge__(self, other):
        """! Перегрузка оператора >="""
        return self.name >= other.name

    def __eq__(self, other):
        """! Перегрузка оператора =="""
        return self.name == other.name
