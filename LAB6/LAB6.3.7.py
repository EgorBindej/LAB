# Функция для преобразования строки
def replace_p_with_stars(s):
    n = len(s)
    half_n = n // 2
    # Преобразуем первые n/2 символов
    modified_first_half = s[:half_n].replace('п', '*')
    # Оствляем вторую половину без изменений
    second_half = s[half_n:]
    # Объединяем модифицированную первую половину и вторую половину
    modified_string = modified_first_half + second_half
    return modified_string

input_string = input("Введите строку: ")

# Преобразование строки
result = replace_p_with_stars(input_string)

print("Преобразованная строка:", result)
