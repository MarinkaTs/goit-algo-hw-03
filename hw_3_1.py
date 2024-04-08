from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        
        # Отримання поточної дати
        current_date = datetime.today().date()
        
        # Отримання різниці між поточною датою та заданою датою
        delta = current_date - date_obj.date()
        
        return delta.days
    except ValueError:
        # Обробка неправильного формату вхідних даних
        return "Неправильний формат дати. Використайте формат 'РРРР-ММ-ДД'."

# Приклад використання:
print(get_days_from_today("2021-10-09"))  


