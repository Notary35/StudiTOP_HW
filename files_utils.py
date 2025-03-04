import pprint
import yaml
import json
import csv


# №1
# Запись в JSON


def write_json(*data: dict, file_name="test.json", encoding: str = "utf-8"):
    with open(file_name, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# №2
# Чтение из JSON


def read_json(file_name="test.json", encoding: str = "utf-8"):
    with open(file_name, "r", encoding=encoding) as f:
        data = json.load(f)
    return data


# №3
# Дозапись в JSON


def append_json(data: dict, file_name="test.json", encoding: str = "utf-8"):

    with open(file_name, "r", encoding=encoding) as f:
        current_data = json.load(f)

    if not isinstance(data, dict):
        raise TypeError("JSON-файл должен содержать словарь")

    current_data.append(data)

    with open(file_name, "w", encoding=encoding) as f:
        json.dump(current_data, f, ensure_ascii=False, indent=4, sort_keys=False)
