# ЗАДАНИЕ 1: Создание и вызов функций
print("ЗАДАНИЕ 1")

def greet(name):
    print(f"Привет, {name}!")

def square(number):
    return number ** 2

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

greet("Маша")
greet("Сергей")
print("Квадрат 5:", square(5))
print("Квадрат 12:", square(12))
print("Максимум из 3 и 7:", max_of_two(3, 7))
print("Максимум из 15 и 9:", max_of_two(15, 9))

# ЗАДАНИЕ 2: Аргументы и возвращаемые значения
print("ЗАДАНИЕ 2")

def calculate_rectangle(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def describe_rectangle(width, height, unit="см"):
    print(f"Прямоугольник: ширина = {width} {unit}, высота = {height} {unit}")
    print(f"Площадь = {calculate_rectangle(width, height)} кв.{unit}")
    print(f"Периметр = {calculate_perimeter(width, height)} {unit}")

describe_rectangle(5, 15)
print()
describe_rectangle(10, 2, unit="м")

# ЗАДАНИЕ 3: Области видимости переменных
print("ЗАДАНИЕ 3")

value = 10

def example():
    value = 20
    local_var = 99
    print(value)

example()
print(value)

try:
    print(local_var)
except NameError as e:
    print("Ошибка:", e)

# ЗАДАНИЕ 4: Работа со списками
print("ЗАДАНИЕ 4")

numbers = [4, 8, 15, 16, 23, 42, 7, 11, 3, 9, 452, -48, 1930, 56, 0]
print("Первый элемент:", numbers[0])
print("Третий элемент:", numbers[2])
print("Последний элемент:", numbers[-1])
numbers[1] = 100
print("После изменения второго элемента:", numbers)
numbers.append(55)
print("После append(55):", numbers)
numbers.remove(15)
print("После remove(15):", numbers)
print("Итоговый список:", numbers)
print("Количество элементов:", len(numbers))

# ЗАДАНИЕ 5: Срезы
print("ЗАДАНИЕ 5")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Первые три:", numbers[:3])
print("Последние три:", numbers[-3:])
print("С 3-го по 7-й:", numbers[2:7])
print("Каждый второй:", numbers[::2])
print("В обратном порядке:", numbers[::-1])

# ЗАДАНИЕ 6: Работа с кортежами
print("ЗАДАНИЕ 6")

measurements = (12, 45, 7, 23, 89, 34, 56, 11, 463, 829, -9, -267, 0)
print("Первый:", measurements[0])
print("Последний:", measurements[-1])
print("Срез [1:5]:", measurements[1:5])

try:
    measurements[0] = 100
except TypeError as e:
    print("Ошибка:", e)

first, second = measurements[0], measurements[1]
print("Первое:", first, "Второе:", second)

temp_list = list(measurements)
temp_list[0] = 100
measurements = tuple(temp_list)
print("Изменённый кортеж:", measurements)

# ЗАДАНИЕ 7: Встроенные функции
print("ЗАДАНИЕ 7")

numbers = [4, 8, -19, -39, 0, 138, 15, 16, 23, 42, 7, 11, 3, 9]
print("Количество:", len(numbers))
print("Сумма:", sum(numbers))
print("Минимум:", min(numbers))
print("Максимум:", max(numbers))
print("Среднее:", sum(numbers) / len(numbers))

sorted_copy = sorted(numbers)
print("Отсортированная копия:", sorted_copy)
print("Исходный список:", numbers)

numbers.sort()
print("После sort():", numbers)

# ЗАДАНИЕ 8: Реализация собственных алгоритмов
print("ЗАДАНИЕ 8")


def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def find_min(numbers):
    minimum = numbers[0]
    for i in numbers:
        if i < minimum:
            minimum = i
    return minimum

def find_max(numbers):
    maximum = numbers[0]
    for o in numbers:
        if o > maximum:
            maximum = o
    return maximum

numbers = [4, 8, 15, 16, -429, -2, 392, 23, 42, 7, 11, 3, 9, 462,]
print("Собственная сумма:", calculate_sum(numbers), "| Встроенная:", sum(numbers))
print("Собственный минимум:", find_min(numbers), "| Встроенный:", min(numbers))
print("Собственный максимум:", find_max(numbers), "| Встроенный:", max(numbers))

# ЗАДАНИЕ 9: Линейный поиск
print("ЗАДАНИЕ 9")


def find_element(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

numbers = [4, 8, 15, 16, 23, 42, 7, 11, 3, 9, 5372, 103, -320, -2, -29]
print("Поиск 23:", find_element(numbers, 23))
print("Поиск 100:", find_element(numbers, 100))

# ЗАДАНИЕ 10: Возврат нескольких значений
print("ЗАДАНИЕ 10")


def analyze(numbers):
    minimum = numbers[0]
    maximum = numbers[0]
    total = 0
    for n in numbers:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
        total += n
    average = total / len(numbers)
    return minimum, maximum, average

numbers = [-10, 3, -2, 8, -5, 573, -99, -32, 33, 268, 1038]
min_val, max_val, avg_val = analyze(numbers)
print("Минимум:", min_val)
print("Максимум:", max_val)
print("Среднее:", avg_val)

# ЗАДАНИЕ 11: Lambda-функции
print("ЗАДАНИЕ 11")

numbers = [-10, 3, -2, 8, -5, -9, 567, 109, 4, 33]
normal_sort = sorted(numbers)
print("Обычная сортировка:", normal_sort)
abs_sort = sorted(numbers, key=lambda x: abs(x))
print("Сортировка по модулю:", abs_sort)

# ЗАДАНИЕ 12: Самостоятельная работа
print("ЗАДАНИЕ 12")

def calculate_average(measurements):
    total = 0
    for n in measurements:
        total += n
    return total / len(measurements)

def find_minimum(measurements):
    minimum = measurements[0]
    for o in measurements:
        if o < minimum:
            minimum = o
    return minimum

def find_maximum(measurements):
    maximum = measurements[0]
    for r in measurements:
        if r > maximum:
            maximum = r
    return maximum

def count_above_average(measurements):
    avg = calculate_average(measurements)
    count = 0
    for u in measurements:
        if u > avg:
            count += 1
    return count

def find_value(measurements, target):
    for i in range(len(measurements)):
        if measurements[i] == target:
            return i
    return -1

def analyze_measurements(measurements):
    return (find_minimum(measurements),
            find_maximum(measurements),
            calculate_average(measurements))

measurements = [12, 45, 7, 23, 89, -90, -2, 0, 34, 56, 11, 78, 5, 789, -64, 326,]
minimum, maximum, average = analyze_measurements(measurements)

print("Количество измерений:", len(measurements))
print("Минимальное значение:", minimum)
print("Максимальное значение:", maximum)
print("Среднее значение:", average)
print("Количество выше среднего:", count_above_average(measurements))

target = int(input("Введите значение для поиска: ")) # это часть где сам вводишь и ищешь а все выше автоматически
result = find_value(measurements, target)
if result != -1:
    print(f"Значение {target} найдено по индексу {result}")
else:
    print(f"Значение {target} не найдено")