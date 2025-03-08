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

car_model = [["Japan", "Toyota", "Mark II"], ["Japan", "Honda", "Civic"]]

append_csv(*car_model)

pprint.pprint(read_csv(), indent=4)
print()


# Тест записи в txt:

from files_utils import write_txt

text = """London is the capital of great Britain.\n"""

write_txt(text)


# Тест чтения из txt:

from files_utils import read_txt

print(read_txt())
print()


# Тест дозаписи в txt:

from files_utils import append_txt

text = """Paris is the capital of France."""

append_txt(text)

print(read_txt())
print()


# Тест записи в YAML:

from files_utils import write_yaml

data = {
    "app_name": "Мое приложение",
    "version": "1.0",
    "admin": "Василий Уткин",
    "settings": {"theme": "dark", "language": "ru", "notifications": True},
    "users": ["admin", "moderator", "guest"],
}

write_yaml(data)


# Тест чтения из YAML:

from files_utils import read_yaml

pprint.pprint(read_yaml(data), indent=4, sort_dicts=False)
print()


# Тест дозаписи в YAML:

from files_utils import append_yaml

data = {
    "extensions": {"name": "Python", "version": "3.10.1", "author": "Michael Jackson"}
}

append_yaml(data)

pprint.pprint(read_yaml(data), width=40, compact=False, sort_dicts=False)
print()


# Тест записи погодного приложения в YAML:

from files_utils import create_weather_config

weather_app_config = {
    "app_name": "Weather Forecast App",
    "version": "2.0",
    "api_key": "your_api_key_here",
    "settings": {
        "default_city": "Moscow",
        "units": "metric",
        "language": "ru",
        "update_interval": 30,
        "notifications": True,
    },
    "display_options": {
        "show_wind": True,
        "show_humidity": True,
        "show_pressure": True,
        "temperature_format": "celsius",
    },
    "supported_features": [
        "current_weather",
        "hourly_forecast",
        "daily_forecast",
        "weather_alerts",
        "weather_maps",
    ],
    "api_endpoints": {
        "base_url": "https://api.weather.com",
        "current": "/current",
        "forecast": "/forecast",
        "alerts": "/alerts",
    },
}

create_weather_config(weather_app_config)


from files_utils import read_weather_config

pprint.pprint(read_weather_config(data), indent=4, sort_dicts=False)
print()
