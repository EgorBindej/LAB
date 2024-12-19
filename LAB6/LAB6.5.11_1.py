def is_prime(num):
    """Проверяет, является ли число простым."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_twin_primes(n):
    """Находит и выводит все пары простых чисел-близнецов на отрезке [n, 2n]."""
    twin_primes = []
    for i in range(n, 2*n - 1):  # Изменено, чтобы пары не выходили за 2n
        if is_prime(i) and is_prime(i + 2):
            if i + 2 <= 2*n:
                twin_primes.append((i, i + 2))
    return twin_primes


n = int(input("Введите натуральное число большее 2: "))

# Поиск и вывод пар простых чисел-близнецов
twin_primes = find_twin_primes(n)
print(f"Пары простых чисел-близнецов на отрезке [{n}, {2*n}]:")
for pair in twin_primes:
    print(pair)
