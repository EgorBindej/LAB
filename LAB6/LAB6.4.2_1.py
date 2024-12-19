
n = int(input("Введите количество элементов массива: "))

array = []
for i in range(n):
    element = int(input(f"Введите элемент {i+1}: "))
    array.append(element)

# Нахождение минимального элемента и его индекса
min_element = min(array)
min_index = array.index(min_element)


print("Индекс минимального элемента:", min_index)

