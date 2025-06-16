from dataclasses import dataclass, field
from typing import List, Dict, Any, Iterator, Optional


@dataclass
class City:
    name: str
    lat: float
    lon: float
    district: str
    population: int
    subject: str

class CitiesIterator:
    """
    Итератор для обработки списка городов с фильтрацией и сортировкой.
    """
    def __init__(self, cities: List[Dict[str, Any]]):
        self._original_data = cities
        self._min_population: Optional[int] = None
        self._sort_by: Optional[str] = None
        self._reverse: Optional[bool] = None
        self._index = 0

    def _validate_city_dict(self, city_dict: Dict[str, Any]):
        """
        Проверяем наличие всех обязательных полей
        """
        required_fields = ["name", "district", "population", "subject", "coords"]
        for field in required_fields:
            if field not in city_dict:
                raise ValueError(f"Отсутствует пункт {field} в городе {city_dict['name']}")
        if 'lat' not in city_dict['coords'] or 'lon' not in city_dict['coords']:
            raise ValueError(f"В пункте 'coords' должны быть подпункты 'lat' и 'lon': {city_dict['name']}")

    def _prepare_cities(self) -> None:
        """
        Преобразуем список городов в список объектоа City
        """
        self._cities: List[City] = []
        for city_dict in self._original_data:
            self._validate_city_dict(city_dict)
            city = City(
                name = city_dict['name'],
                lat = float(city_dict['coords']['lat']),
                lon = float(city_dict['coords']['lon']),
                district = city_dict['district'],
                population = int(city_dict['population']),
                subject = city_dict['subject']
            )
            if self._min_population is None or city.population >= self._min_population:
                self._cities.append(city)
        if self._sort_by:
            self._cities.sort(key=lambda city: getattr(city, self._sort_by), reverse=self._reverse)
            
    def set_population_filter(self, min_population: int) -> None:
        """
        Фильтр минимального населения
        """
        self._min_population = min_population
        self._prepare_cities()
        
    def sort_by(self, parametr: str, reverse: bool = False) -> None:
        """
        Сортировка по параметрам
        """
        if parametr not in City.__dataclass_fields__:
            raise ValueError(f"Некорректный параметр сортировки: {parametr}")
        self._sort_by = parametr
        self._reverse = reverse
        self._prepare_cities()

    def __iter__(self) -> Iterator[City]:
        """
        Итератор списка
        """
        self._index = 0
        return self

    def __next__(self) -> City:
        """
        Возвращает следующий город из списка.
        """
        if self._index >= len(self._cities):
            raise StopIteration
        city = self._cities[self._index]
        self._index += 1
        return city

# Тест
cities_list = [
    {
        "coords": {"lat": "52.65", "lon": "90.08333"},
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия"
    },
    {
        "coords": {"lat": "55.75", "lon": "37.61667"},
        "district": "Центральный",
        "name": "Москва",
        "population": 12615882,
        "subject": "Москва"
    }
]
def main():
    cities_iterator = CitiesIterator(cities_list)
    cities_iterator.set_population_filter(10000)
    cities_iterator.sort_by("name")

    for i in range(2):
        print(next(cities_iterator))

if __name__ == "__main__":
    main()