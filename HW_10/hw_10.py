"""
# Домашнее задание №10📃
## Часть 1: Декоратор для валидации пароля
"""
from typing import Callable
import csv

special_symbols_set = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '~', '`', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/'}

# user_password = str(input("Создайте пароль: "))


def password_checker(length: int = 8) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(password: str):
            errors = []
            if len(password) < length:
                errors.append("• Пароль должен быть не менее 8 символов")
            if set(password) & special_symbols_set == set():
                special_symbols_list = list(special_symbols_set)
                errors.append(f"• Пароль должен содержать хотя-бы один спец-символ: ({', '.join(special_symbols_list[:5])}) и т.д.")
            if not any (simbol.isalpha() for simbol in password):
                errors.append("• Пароль должен содержать буквенные символы")
            if not any (simbol.isupper() for simbol in password):
                errors.append("• Пароль должен содержать хотя-бы одну заглавную букву")
            if not any (simbol.islower() for simbol in password):
                errors.append("• Пароль должен содержать хотя-бы одну строчную букву")
            if not any(simbol.isdigit() for simbol in password):
                errors.append("• Пароль должен содержать хотя-бы одну цифру")
            if " " in password:
                errors.append("• Пароль не должен содержать пробелы")
            if errors:
                raise ValueError("\n".join(errors))
            return func(password)
        return wrapper
    return decorator

@password_checker()
def register_user1(password: str) -> str:
    return (f'Пароль "{password}" принят!')

# while True: # Добавил цикл от себя
#     user_password = input("Создайте пароль: ")
#     try:
#         print(register_user1(user_password))
#         break
#     except ValueError as e:
#         print(f"Ошибка:\n{e}\nПовторите попытку\n")

# Домашнее задание №10📃
# Часть 2: Декоратор для валидации электронной почты

def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1):
    """Декоратор валидации пароля c минимальными требованиями"""
    def decorator(func: Callable) -> Callable:
        def wrapper(password: str, username: str):
            errors = []
            if len(password) < length:
                errors.append("• Пароль должен быть не менее 8 символов")
            if sum(1 for simbol in password if simbol.isupper()) < uppercase:
                errors.append("• Пароль должен содержать хотя-бы одну заглавную букву")
            if sum(1 for simbol in password if simbol.islower()) < lowercase:
                errors.append("• Пароль должен содержать хотя-бы одну строчную букву")
            if sum(1 for simbol in password if simbol in special_symbols_set) < special_chars:
                special_symbols_list = list(special_symbols_set)
                errors.append(f"• Пароль должен содержать хотя-бы один спец-символ: ({', '.join(special_symbols_list[:5])}) и т.д.")
            if errors:
                raise ValueError("\n".join(errors))
            return func(username, password)
        return wrapper
    return decorator

def username_validator() -> Callable:
    """Декоратор валидации имени пользователя p.s. с проверкой на пробелы"""
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str):
            if " " in username:
                raise ValueError("• Имя пользователя не должно содержать пробелы")
            return func(username, password)
        return wrapper
    return decorator

@username_validator()
@password_validator()
def register_user(username: str, password: str, file_name = "users.csv"):
    """Функция регистрации пользователя с внесемнием данных в CSV файл"""
    with open(file_name, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

while True:
    """Цикл регистрации пользователя с обработкой ошибок"""
    username = input("Введите имя пользователя: ")
    password = input(str("Введите пароль: "))
    try:
        register_user(username, password)
        print(f'Пользователь "{username}" зарегистрирован!')
        break
    except ValueError as e:
        print(f"Ошибка:\n{e}\nПовторите попытку\n")