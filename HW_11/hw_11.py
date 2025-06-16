from dataclasses import dataclass, field
from typing import List, Dict, Any, Iterator, Optional
import json


@dataclass
class City:
    name: str
    lat: float
    lon: float
    district: str
    population: int
    subject: str

class CitiesIterator:
    def __init__(self, cities: List[Dict[str, Any]]):
        self._original_data = cities
        self._min_population: Optional[int] = None
        self._sort_by: Optional[str] = None
        self._reverse: Optional[bool] = None
        self._index = 0

    def _validate_city_dict(self, city_dict: Dict[str, Any]):
        required_fields = ["name", "district", "population", "subject", "coords"]
        for field in required_fields:
            if field not in city_dict:
                raise ValueError(f"Отсутствует пункт {field} в городе {city_dict['name']}")
        if 'lat' not in city_dict['coords'] or 'lon' not in city_dict['coords']:
            raise ValueError(f"В пункте 'coords' должны быть подпункты 'lat' и 'lon': {city_dict['name']}")


    def sort_by(self, parametr: str, reverse: bool = False) -> None:
        if not hasattr(City, parametr):
            raise ValueError(f"Некорректный параметр {parametr}")
        self._sort_by = parametr
        self._reverse = reverse

    def __next__(self) -> City:
        if self._index >= len(self._cities):
            raise StopIteration
        city = self._cities[self._index]
        self._index += 1
        return city