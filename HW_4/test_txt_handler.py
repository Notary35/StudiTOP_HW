from txt_file_handler import TxtFileHandler

handler = TxtFileHandler()

# Тест записи в файл:

text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
"""

handler.write_file("test.txt", text)


# Тест дозаписи в файл:

new_text = """
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
"""

handler.append_file("test.txt", new_text)


# Тест чтения из файла:

handler.read_file("test.txt")
result = handler.read_file("test.txt")
print(type(result))
print(result)