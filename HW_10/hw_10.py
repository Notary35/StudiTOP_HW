"""
# Домашнее задание №10📃
## Часть 1: Декоратор для валидации пароля
"""
from typing import Callable

special_symbols_set = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '~', '`', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/'}

user_password = str(input("Создайте пароль: "))


def password_checker(length: int = 8) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(password: str):
            errors = []
            if len(password) < length:
                errors.append("Пароль должен быть не менее 8 символов")
            if set(password) & special_symbols_set == set():
                special_symbols_list = list(special_symbols_set)
                errors.append(f"Пароль должен содержать хотя-бы один спец-символ: {', '.join(special_symbols_list[:5])} и т.д.")
            if not any (simbol.isalpha() for simbol in password):
                errors.append("Пароль должен содержать буквенные символы")
            if not any (simbol.isupper() for simbol in password):
                errors.append("Пароль должен содержать хотя-бы одну заглавную букву")
            if not any (simbol.islower() for simbol in password):
                errors.append("Пароль должен содержать хотя-бы одну строчную букву")
            if not any(simbol.isdigit() for simbol in password):
                errors.append("Пароль должен содержать хотя-бы одну цифру")
            if " " in password:
                errors.append("Пароль не должен содержать пробелы")
            if errors:
                raise ValueError("\n".join(errors))
            return func(password)
        return wrapper
    return decorator

@password_checker()
def register_user(password: str) -> str:
    return (f'Пароль "{password}" принят!')

print(register_user(user_password))
