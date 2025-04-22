# №1
from typing import Dict, Any, List, Set, Union
from pprint import pprint
from marvel import full_dict

# №2
user_num = input("Введите номера фильмов через пробел(от 1 до 42): ")

def user_inp(value: str):
    if not value.isdigit() or int(value) < 1 or int(value) > 42:
        return None
    return int(value)

user_list: List[Union[int, None]] = list(map(user_inp, user_num.split()))

# №3
simple_list: List[Dict[str, Any]] = []

for index, film in full_dict.items():
    simple_list.append({"id": index, **film})

simple_list = sorted(simple_list, key=lambda film: film["id"])

result_list: List[Dict[str, Any]] = list(filter(lambda film: film["id"] in user_list, simple_list))

result_dict: Dict[int, Dict[str, Any]] = {film["id"]: film for film in result_list}

print("Результат задания №3: Словарь с исходными id и другими ключами для фильмов из списка")
pprint(result_dict, sort_dicts=False)
print()

# №4
unique_directors: Set[str] = {film["director"] for film in result_dict.values()}

print("Результат задания №4: Уникальные режиссеры")
pprint(unique_directors)
print()

# №5
full_dict_copy: Dict[Any, Dict[str, Any]] = {
    key: {**value, "year": str(value["year"])} for key, value in full_dict.items()
}

print("Результат задания №5: Копия словаря с преобразованным 'year' в строку")
pprint(full_dict_copy, sort_dicts=False)
print()

# №6
sorted_set: Dict[Any, Dict[str, Any]] = dict(
    filter(lambda film: film[1].get("title") and film[1]["title"].lower().startswith("ч"), full_dict.items())
)

print("Результат задания №6: Фильмы, начинающиеся на 'Ч'")
pprint(sorted_set, sort_dicts=False)
print()

# №7
sorted_set2: Dict[Any, Dict[str, Any]] = dict(
    sorted(
        full_dict.items(),
        key=lambda film: (
            int(film[1].get("year", 0))
            if isinstance(film[1].get("year"), int) or str(film[1].get("year")).isdigit()
            else 0
        ),
        reverse=True,
    )
)

print("Результат задания №7: Фильмы, отсортированные по году от большего к меньшему")
pprint(sorted_set2, sort_dicts=False)
print()

# №8
stage_list: Dict[str, int] = {
    "Первая фаза": 1,
    "Вторая фаза": 2,
    "Третья фаза": 3,
    "Четвёртая фаза": 4,
    "Пятая фаза": 5,
    "Шестая фаза": 6,
}

sorted_set3: Dict[Any, Dict[str, Any]] = dict(
    sorted(
        full_dict.items(),
        key=lambda film: (
            (
                int(film[1].get("year", float("inf")))
                if isinstance(film[1].get("year"), int) or str(film[1].get("year")).isdigit()
                else float("inf")
            ),
            stage_list.get(film[1].get("stage", ""), float("inf")),
        ),
    )
)

print("Результат задания №8: Фильмы, отсортированные по фазам и году от меньшего к большему")
pprint(sorted_set3, sort_dicts=False)
print()

# №9
sorted_set4: Dict[Any, Dict[str, Any]] = dict(
    sorted(
        filter(
            lambda film: film[1].get("title") and "мстители" in film[1]["title"].lower(),
            full_dict.items(),
        ),
        key=lambda film: (stage_list.get(film[1].get("stage", ""), 0), film[1].get("title")),
    )
)

print("Результат задания №9: Фильмы с 'Мстителями' в названии, отсортированные по фазам")
pprint(sorted_set4, sort_dicts=False)
print()

# №10 Проверка mypy пройдена успешно.