import pprint




# Протестируем функцию записи JSON
from files_utils import write_json

persons = [
    {"name": "Adolf", "age": 56, "city": "Braunau am Inn"},
    {"name": "Joseph", "age": 74, "city": "Gori"},
    {"name": "Vladimir", "age": 53, "city": "Ulyanovsk"},
]

# write_json(person)
write_json(*persons)

# Протестируем чтение из JSON

from files_utils import read_json

# read_json = list(read_json())

pprint.pprint(read_json(), indent=4, sort_dicts=False)
print()

# Протестируем дозапись из JSON и после прочитаем обновлённый словарь

from files_utils import append_json

person = {"name": "Benito", "age": 61, "city": "Predappio"}

append_json(person)

pprint.pprint(read_json(), indent=4, sort_dicts=False)
print()

# Тест записи в CSV:

from files_utils import write_csv

car_models = [
    ["Germany", "Audi", "A4"],
    ["Germany", "BMW", "X5"],
    ["Germany", "Mercedes", "C63"],
    ["Italy", "Lamborghini", "Aventador"],
    ["United Kingdom", "Rolls-Royce", "Phantom"],
    ["France", "Bugatti", "Chiron"],
    ["Italy", "Pagani", "Huayra"],
    ["Italy", "Ferrari", "F430"],
]

write_csv(*car_models)

# Тест чтения из CSV:

from files_utils import read_csv

pprint.pprint(read_csv(), indent=4)
print()

# Тест дозаписи в CSV:

from files_utils import append_csv

car_model = [
    ["Japan", "Toyota", "Mark II"],
    ["Japan", "Honda", "Civic"]
]

append_csv(car_model)

pprint.pprint(read_csv(), indent=4)
print()