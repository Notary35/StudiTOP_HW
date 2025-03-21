from file_classes import TxtFile, JsonFile, CsvFile
import pprint

if __name__ == "__main__":

    txt = TxtFile("test.txt")

    text = "- Что мы говорим богу смерти?\n"
    txt.write_file(text)

    text = "- Не сегодня"
    txt.append_file(text)

    result = txt.read_file()
    print(type(result))
    print()
    print(result)
    print()

    json = JsonFile("test.json")
    data = [
        "Серсея Ланнистер",
        "Джон Сноу",
        "Тирион Ланистер",
        "Дайенерис Таргариен",
        "Сандор Клиган",
        "Джейме Ланистер",
        "Джон Аррен",
        "Санса Старк",
    ]
    json.write_file(data)

    data = ["Эддард Старк", "Робб Старк", "Ария Старк", "Ария Старк"]
    json.append_file(data)

    result = json.read_file()
    print(type(result))
    print()
    pprint.pprint(result)
    print()

    csv = CsvFile("test.csv")
    data = [
        {"name": "Серсея Ланнистер", "age": 43, "birthplace": "Королевская Гавань"},
        {"name": "Джон Сноу", "age": 22, "birthplace": "Винтерфелл"},
        {"name": "Тирион Ланистер", "age": 30, "birthplace": "Королевская Гавань"},
        {"name": "Дайенерис Таргариен", "age": 25, "birthplace": "Драконий камень"},
    ]

    csv.write_file(data)

    data = [
        {"name": "Сандор Клиган", "age": 35, "birthplace": "Королевская Гавань"},
        {"name": "Джейме Ланистер", "age": 35, "birthplace": "Королевская Гавань"},
        {"name": "Джон Аррен", "age": 60, "birthplace": "Орлиное гнездо"},
        {"name": "Санса Старк", "age": 20, "birthplace": "Винтерфелл"},
    ]
    csv.append_file(data)

    result = csv.read_file()

    pprint.pprint(result, indent=4, width=120, sort_dicts=False)
