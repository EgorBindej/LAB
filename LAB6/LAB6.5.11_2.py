def find_max_index(arr, n):
    
    if n == 1:
        return 0

    # Рекурсивный вызов для поиска индекса максимального элемента в подмассиве
    max_index_rest = find_max_index(arr, n - 1)

   
    if arr[n - 1] > arr[max_index_rest]:
        return n - 1
    else:
        return max_index_rest


n = int(input("Введите размер массива: "))


array = []
for i in range(n):
    element = int(input(f"Введите элемент {i+1}: "))
    array.append(element)


max_index = find_max_index(array, n)


print("Индекс максимального элемента:", max_index)

