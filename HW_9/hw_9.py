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