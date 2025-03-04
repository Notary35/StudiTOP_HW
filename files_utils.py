import pprint
import yaml
import json
import csv


# Запись в JSON:

def write_json(*data: dict, file_name="test.json", encoding: str = "utf-8"):
    with open(file_name, "w", encoding=encoding) as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# Чтение из JSON:

def read_json(file_name="test.json", encoding: str = "utf-8"):
    with open(file_name, "r", encoding=encoding) as f:
        data = json.load(f)
    return data


# Дозапись в JSON:

def append_json(data: dict, file_name="test.json", encoding: str = "utf-8"):

    with open(file_name, "r", encoding=encoding) as f:
        current_data = json.load(f)

    if not isinstance(data, dict):
        raise TypeError("JSON-файл должен содержать словарь")

    current_data.append(data)

    with open(file_name, "w", encoding=encoding) as f:
        json.dump(current_data, f, ensure_ascii=False, indent=4, sort_keys=False)


# Запись в CSV:

def write_csv(*data: list, file_name="test.csv", encoding: str = "utf-8-sig"):
    with open(file_name, "w", encoding=encoding) as f:
        writer = csv.writer(f, delimiter=";", lineterminator='\n')
        writer.writerows(data)


# Чтение из CSV:

def read_csv(file_name="test.csv", encoding: str = "utf-8-sig"):
    with open(file_name, "r", encoding=encoding) as f:
        data = list(csv.reader(f, delimiter=";"))
    return data


# Дозапись в CSV:

def append_csv(data: list, file_name="test.csv", encoding: str = "utf-8-sig"):
    with open(file_name, "a", encoding=encoding) as f:
        writer = csv.writer(f, delimiter=";", lineterminator='\n')
        writer.writerows(data)
