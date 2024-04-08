from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)
        
        # Перевірка, чи день народження вже минув у цьому році
        if birthday < today:
            # Якщо так, розглядаємо дату на наступний рік
            birthday = birthday.replace(year=today.year + 1)
        
        # Визначення різниці між днем народження та поточним днем
        days_until_birthday = (birthday - today).days
        
        # Перевірка, чи день народження припадає на вихідний
        if (today + timedelta(days_until_birthday)).weekday() in [5, 6]:  # 5 та 6 - субота та неділя
            # Якщо так, перенесення дати привітання на наступний понеділок
            days_until_birthday += (7 - (today + timedelta(days_until_birthday)).weekday())
        
        # Додавання інформації про користувача та дату привітання до результату
        congratulation_date = today + timedelta(days_until_birthday)
        upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
    
    return upcoming_birthdays

# Приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
