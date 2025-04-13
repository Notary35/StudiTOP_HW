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


class CityGame:
    def __init__(self, cities: List[City]):
        self.cities = cities
        self.used_cities = []
        self.current_letter = None

    def start_game(self):
        print("Игра началась!")
        available_cities = [city for city in self.cities if not city.is_used]
        if available_cities:
            first_city = random.choice(available_cities)
            self.mark_city_as_used(first_city.name)
            self.current_letter = self.get_last_valid_letter(first_city.name)
            print(f"Компьютер назвал город: {first_city.name}. Следующая буква: {self.current_letter}")
        else:
            print("Нет доступных городов для начала игры.")

    def human_turn(self, city_name: str):
        city_name = city_name.title()
        if not self.is_valid_city(city_name):
            print(f"Город {city_name} не найден или уже использован.")
            return
        self.mark_city_as_used(city_name)
        self.current_letter = self.get_last_valid_letter(city_name)
        print(f"Вы назвали город: {city_name}. Следующая буква: {self.current_letter}")
        self.computer_turn()

    def computer_turn(self):
        for city in self.cities:
            if not city.is_used and self.current_letter and city.name.lower().startswith(self.current_letter):
                self.mark_city_as_used(city.name)
                self.current_letter = self.get_last_valid_letter(city.name)
                print(f"Компьютер назвал город: {city.name}. Следующая буква: {self.current_letter}")
                return
        print("Компьютер не смог найти город. Вы победили!")

    def is_valid_city(self, city_name: str) -> bool:
        for city in self.cities:
            if city.name == city_name and not city.is_used:
                return True
        return False

    def mark_city_as_used(self, city_name: str):
        for city in self.cities:
            if city.name == city_name:
                city.is_used = True
                self.used_cities.append(city_name)
                break

    def get_last_valid_letter(self, city_name: str) -> str:
        for letter in reversed(city_name):
            if not is_bad_letter(letter):
                return letter.lower()
        return None


class GameManager:
    def __init__(self, cities_file_path: str):
        self.json_file = JsonFile(cities_file_path)
        city_data = self.json_file.read_data()
        if city_data is None:
            raise ValueError("Данные о городах отсутствуют.")
        self.cities_serializer = CitiesSerializer(city_data)
        self.city_game = CityGame(self.cities_serializer.get_all_cities())

    def run_game(self):
        """Я сказала 'Стартуем' - Наталья Морская Пехота"""
        self.city_game.start_game()
        while True:
            city_name = input("Введите название города или 'выход' для завершения игры: ")
            if city_name.lower() == "выход":
                print("Игра завершена.")
                break
            self.city_game.human_turn(city_name)


if __name__ == "__main__":
    cities_file_path = "cities.json"
    game_manager = GameManager(cities_file_path)
    game_manager.run_game()