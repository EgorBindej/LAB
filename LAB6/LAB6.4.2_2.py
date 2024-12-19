
n = int(input("Введите количество элементов массива: "))


array = []
for i in range(n):
    element = int(input(f"Введите элемент {i+1}: "))
    array.append(element)

# Инициализация второго и третьего массивов
positive_array = []
negative_array = []

# Переписывание элементов в соответствующие массивы
for element in array:
    if element > 0:
        positive_array.append(element)
    else:
        negative_array.append(element)


print("Положительные элементы:", positive_array)
print("Остальные элементы:", negative_array)

