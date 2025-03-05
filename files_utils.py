import pprint
import yaml
import json
import csv

# import pylance


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
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerows(data)


# Чтение из CSV:


def read_csv(file_name="test.csv", encoding: str = "utf-8-sig"):
    with open(file_name, "r", encoding=encoding) as f:
        data = list(csv.reader(f, delimiter=";"))
    return data


# Дозапись в CSV:


def append_csv(*data: list, file_name="test.csv", encoding: str = "utf-8-sig"):
    with open(file_name, "a", encoding=encoding) as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerows(data)


# Запись в txt:


def write_txt(data: str, file_name="test.txt", encoding: str = "utf-8"):
    with open(file_name, "w", encoding=encoding) as f:
        f.write(data)


# Чтение из txt:


def read_txt(file_name="test.txt", encoding: str = "utf-8"):
    with open(file_name, "r", encoding=encoding) as f:
        data = f.read()
    return data


# Дозапись в txt:


def append_txt(data, file_name="test.txt", encoding: str = "utf-8"):
    with open(file_name, "a", encoding=encoding) as f:
        f.write(data)


# Запись в YAML:


def write_yaml(data, file_name="test.yaml", encoding: str = "utf-8"):
    with open(file_name, "w", encoding=encoding) as f:
        yaml.dump(
            data, f, default_flow_style=False, allow_unicode=True, sort_keys=False
        )


# Чтение в YAML:


def read_yaml(data, file_name="test.yaml", encoding: str = "utf-8"):
    with open(file_name, "r", encoding=encoding) as f:
        data = yaml.safe_load(f)
    return data


# Дозапись в YAML:


def append_yaml(data, file_name="test.yaml", encoding: str = "utf-8"):
    with open(file_name, "a", encoding=encoding) as f:
        yaml.dump(
            data, f, default_flow_style=False, allow_unicode=True, sort_keys=False
        )


# Запишем функцию для создания и чтения погодного приложения в YAML:


def create_weather_config(
    data, file_name="weather_app_config.yaml", encoding: str = "utf-8"
):
    with open(file_name, "w", encoding=encoding) as f:
        yaml.dump(
            data, f, default_flow_style=False, allow_unicode=True, sort_keys=False
        )


def read_weather_config(
    data, file_name="weather_app_config.yaml", encoding: str = "utf-8"
):
    with open(file_name, "r", encoding=encoding) as f:
        data = yaml.safe_load(f)
    return data
