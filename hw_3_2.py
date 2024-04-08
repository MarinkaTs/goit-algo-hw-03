import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка валідності вхідних даних
    if not (1 <= min_num <= max_num <= 1000):
        return []

    # Генерація випадкових унікальних чисел у межах заданого діапазону
    unique_numbers = random.sample(range(min_num, max_num + 1), min(quantity, max_num - min_num + 1))
    
    # Сортування чисел та повернення результату
    return sorted(unique_numbers)

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
