from files_utils import write_json
import pprint


persons = [
    {"name": "Adolf", "age": 56, "city": "Braunau am Inn"},
    {"name": "Joseph", "age": 74, "city": "Gori"},
    {"name": "Vladimir", "age": 53, "city": "Ulyanovsk"},
]

# Протестируем функцию записи
# write_json(person)
write_json(*persons)

# Протестируем чтение из JSON

from files_utils import read_json

# read_json = list(read_json())

pprint.pprint(read_json(), indent=4, sort_dicts=False)

# Протестируем дозапись из json и после прочитаем обновлённый словарь

from files_utils import append_json

person = {"name": "Benito", "age": 61, "city": "Predappio"}

append_json(person)

pprint.pprint(read_json(), indent=4, sort_dicts=False)
