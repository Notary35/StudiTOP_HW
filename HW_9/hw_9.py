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