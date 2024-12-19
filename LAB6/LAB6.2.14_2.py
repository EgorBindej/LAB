
def calculate_y(x):
    return -0.5 * x + x

# Ввод параметров
min_x = float(input("Введите минимум для x: "))
max_x = float(input("Введите максимум для x: "))
step = float(input("Введите шаг: "))

# Заголовок таблицы
print(f"{'x':>6} {'y':>6}")

# Вычисление и вывод значений
x = min_x
while x <= max_x:
    y = calculate_y(x)
    print(f"{x:>6} {y:>6.2f}")
    x += step
