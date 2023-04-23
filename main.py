"""!В данном модуле генерируем наборы данных различной размерности.
Далее записываем их в .xlsx. Затем считываем их из файла, сортируем и
сохраняем в новых файлах. С помощью таймера засекаем время работы функций сортировок.
"""
import copy
import timeit
import pandas as pd
from collections import defaultdict
from russian_names import RussianNames

from Employee import Employee
from Generation import generation

from Find_algorithms import merge_sort
from Find_algorithms import simple_search
from Find_algorithms import binary_search

""" размерности наборов данных для генерации"""
size = [500, 1000, 2000, 3000, 4000, 5000, 8000, 10000]

# """! Запись сгенерированных файлов в файл"""
# with pd.ExcelWriter("./Employees.xlsx") as writer:
#     for i in size:
#         pd.DataFrame(generation(i)).to_excel(writer, sheet_name=f"{i}", index=False)

"""" Читаем из файла и записываем в словарь"""
employees = {}
for i in size:
    c = pd.read_excel('./Employees.xlsx', sheet_name=f'{i}').to_dict('records')
    c_employees = []
    for empl in c:
        c_employees.append(
            Employee(empl['ФИО'], empl['Должность'], empl['Отдел'], empl['Зарплата, руб.'])
        )
    employees[i] = c_employees

""" списки для хранения времени"""
time_simple = []
time_binary = []
time_binary_sort = []
time_key = []

""" сортировка данных, считанных из файла .xlsx"""
for j in size:
    names = [k.name for k in employees[j]]
    key = Employee(RussianNames(count=1,surname=False).get_batch()[0],'','',30000)

    #Поиск по ключу в массиве
    employee_multi_map = defaultdict(list)
    for employee in employees[j]:
        employee_multi_map[employee.name].append(employee)
    start1 = timeit.default_timer()
    print([(i.name, i.pos, i.dep, i.sal) for i in employee_multi_map[key.name]])
    end1 = timeit.default_timer() - start1
    time_key.append(end1)

    # Простой поиск
    start2 = timeit.default_timer()
    simple_search(employees[j], key)
    end2 = timeit.default_timer() - start2
    time_simple.append(end2)

    # Бинарный поиск с сортировкой
    start3 = timeit.default_timer()
    merge_sort(employees[j], 0, len(employees[j]) - 1)
    binary_search(employees[j], 0, len(employees[j]), key)
    end3 = timeit.default_timer() - start3
    time_binary_sort.append(end3)

    """Бинарный поиск"""
    start4 = timeit.default_timer()
    binary_search(employees[j], 0, len(employees[j]), key)
    end4 = timeit.default_timer() - start4
    time_binary.append(end4)

print(f'time_simple = {time_simple}')
print(f'time_binary = {time_binary}')
print(f'time_binary_sort = {time_binary_sort}')
print(f'time_key = {time_key}')

