import json
from typing import List, Dict, Any
from dataclasses import dataclass
import random


class JsonFile:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_data(self) -> Any:
        """Читает данные из JSON-файла и возвращает их."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Файл {self.file_path} не найден.")
            return None
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {self.file_path}.")
            return None


@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False


bad_letters = {"ь", "ъ", "ы"}


def is_bad_letter(letter: str) -> bool:
    return letter in bad_letters


