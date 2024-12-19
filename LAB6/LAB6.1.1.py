
def check_number(num):
    if 1 <= num <= 3:
        print(num)


numbers = []
for i in range(3):
    number = int(input(f"Введите целое число {i+1}: "))
    numbers.append(number)


for num in numbers:
    check_number(num)
