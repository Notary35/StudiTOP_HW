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


class CitiesSerializer:
    def __init__(self, city_data: List[dict]):
        self.cities = [
            City(
                name=city["name"],
                population=city["population"],
                subject=city["subject"],
                district=city["district"],
                latitude=float(city["coords"]["lat"]),
                longitude=float(city["coords"]["lon"]),
                is_used=False
            )
            for city in city_data
        ]

    def get_all_cities(self) -> List[City]:
        return self.cities